"""
This should be run on PySpark Shell.
"""

# Get text file as RDD
rdd = sc.textFile("downloads/lab4/data.txt")

# Get words
words_rdd = rdd.flatMap(lambda x: x.split(" "))

# Match words with it's length
pair_rdd = words_rdd.map(lambda x: (x, len(x)))

# Leave only words with length 7
len7_rdd = pair_rdd.filter(lambda (x, y): y == 7)  # Only works in Python2

# Sort by key descending
sort_rdd = len7_rdd.sortByKey(0)  # For some reason this can't be the last

# Drop the length
words7_rdd = sort_rdd.map(lambda (x, y): x)  # Only works in Python2

# Do again with data2.txt
data2_rdd = sc.textFile("downloads/lab4/data.txt") \
    .flatMap(lambda x: x.split(" ")).map(lambda x: (x, len(x))) \
    .filter(lambda (x, y): y == 7).sortByKey(0).map(lambda (x, y): x)

# Save output
words7_rdd.saveAsTextFile("hdfs://localhost:9000/output4_1")
data2_rdd.saveAsTextFile("hdfs://localhost:9000/output4_2")

# Download output
# $HADOOP_HOME/bin/hdfs dfs -cat /output4_1 /output4_1/part-00000
# $HADOOP_HOME/bin/hdfs dfs -getmerge /output4_1 results/exercise4_1_1.txt
# $HADOOP_HOME/bin/hdfs dfs -cat /output4_2 /output4_2/part-00000
# $HADOOP_HOME/bin/hdfs dfs -getmerge /output4_2 results/exercise4_1_2.txt
