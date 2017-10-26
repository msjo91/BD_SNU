## Java Virtual Machine Process Status Tool
```
jps
```
## Spark
#### Run
```
$SPARK_HOME/sbin/start-all.sh
```
#### Open shell
```
$SPARK_HOME/bin/pyspark
```
#### Close
```
$SPARK_HOME/sbin/stop-all.sh
```
## Hadoop
#### Run
```
$HADOOP_HOME/sbin/start-all.sh
```
#### Make directory in hadoop
```
$HADOOP_HOME/bin/hdfs dfs -mkdir /path/in/hadoop
```
#### Put in hadoop
```
$HADOOP_HOME/bin/hdfs dfs -put <file> /path/in/hadoop
```
#### Save in hadoop
Open spark-shell

```
<RDD>.saveAsTextFile("hdfs://localhost:9000/<name>")
```
#### Download to local
```
$HADOOP_HOME/bin/hdfs dfs -cat /path/in/hadoop /path/in/hadoop/part-00000
$HADOOP_HOME/bin/hdfs dfs -getmerge /path/in/hadoop <name>.txt
```
#### Delete from hadoop
```
$HADOOP_HOME/bin/hdfs dfs -rm -r /path/in/hadoop
```
#### Browse
Open browser

```
localhost:50070
```
#### Close
```
$HADOOP_HOME/sbin/stop-dfs.sh
```
