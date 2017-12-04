#!/bin/bash

benchmark=("wordcount" "sort")
master="localhost"

# ===============================================================
# =       Set benchmark number what you want to test            =
# =                0 : wordcount, 1: sort                       =
# ===============================================================
benchtest=(0 1)

# ===============================================================
# =    Set your own parameters (wordcount terasort pagerank)    =
# =       parallelism: number of partitions in one RDD          =
# =       driver_mem: Siae of memory for master node            =
# =       worker_mem: Size of memory for worker                 =
# =       worker_inst: Number of worker per slave node          =
# =       cores: Number of core per worker                      =
# ===============================================================
parallelism=(4 4)
driver_mem=(2g 2g)
worker_mem=(10g 10g)
worker_inst=(64 64)
cores=(1 1)


# ===============================================================
# =           (CAUTION) DO NOT TOUCH UNDER THIS LINE            =
# ===============================================================
spark="/usr/local/spark/"
hadoop="/usr/local/hadoop/"
hdfs="hdfs://"$master":9000/"
sparkmaster="spark://"$master":7077"

base_parallelism=(4 4)
base_worker_mem=(2g 2g)
base_driver_mem=(2g 2g)
base_worker_inst=(2 2)
base_cores=(1 1)

geomean_waspA=(93 17)
geomean_waspB=(-43 34)

init() {
  core=$1
  mem=$2
  inst=$3
  $spark/sbin/stop-all.sh
  sed -i "3s/.*/export SPARK_WORKER_CORES=$core/g" $spark/conf/spark-env.sh
  sed -i "4s/.*/export SPARK_WORKER_MEMORY=$mem/g" $spark/conf/spark-env.sh
  sed -i "5s/.*/export SPARK_WORKER_INSTANCES=$inst/g" $spark/conf/spark-env.sh
  $spark/sbin/start-all.sh
}

for i in ${benchtest[@]}
do
    hdfs_bench=$hdfs${benchmark[i]}
    $hadoop/bin/hdfs dfs -rmr $hdfs_bench/output

    init ${base_cores[i]} ${base_worker_mem[i]} ${base_worker_inst[i]}
    beginTime=$(date +%s%N)
    $spark/bin/spark-submit \
        --master $sparkmaster \
        --conf spark.default.parallelism=${base_parallelism[i]} \
        --conf spark.driver.memory=${base_driver_mem[i]} \
        --conf spark.executor.memory=${base_worker_mem[i]} \
        --conf spark.executor.cores=${base_cores[i]} \
        ${benchmark[i]}/${benchmark[i]}_base.py $hdfs_bench $hdfs_bench/output
    sleep 1
    endTime=$(date +%s%N)
    elapsed_base[i]=`echo "($endTime - $beginTime) / 1000000" | bc`

    $hadoop/bin/hdfs dfs -rmr $hdfs_bench/output

    init ${cores[i]} ${worker_mem[i]} ${worker_inst[i]}
    beginTime=$(date +%s%N)
    $spark/bin/spark-submit \
        --master $sparkmaster \
        --conf spark.default.parallelism=${parallelism[i]} \
        --conf spark.driver.memory=${driver_mem[i]} \
        --conf spark.executor.memory=${worker_mem[i]} \
        --conf spark.executor.cores=${cores[i]} \
        ${benchmark[i]}/${benchmark[i]}.py $hdfs_bench $hdfs_bench/output
    sleep 1
    endTime=$(date +%s%N)
    elapsed_test[i]=`echo "($endTime - $beginTime) / 1000000" | bc`

    $hadoop/bin/hdfs dfs -rmr $hdfs_bench/output
done

for i in ${benchtest[@]}
do
    score=`echo ${geomean_waspA[i]}\*${elapsed_base[i]}/${elapsed_test[i]}+${geomean_waspB[i]} | bc -l`
    echo "Your score of ${benchmark[i]} is $score / 100"
done
