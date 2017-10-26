"""
pyspark needed.
Must be run in spark-shell.
"""

# Get file from hadoop
rdd = sc.textFile("hdfs://localhost:9000/input")

# Split words
flat = rdd.flatMap(lambda line: line.split(" "))

# Total count
counts = flat.count()
# Count per word (word, count)
wordcounts = flat.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
# Sort (ascend by key)
sortcounts = wordcounts.sortBy(lambda x: x[0])
# Top 5 count (descend by value)
topcounts = wordcounts.takeOrdered(5, lambda x: -x[1])

# Bigram count
bicounts = rdd.map(lambda line: line.split(" ")) \
    .flatMap(lambda x: list(((x[i], x[i + 1]), 1) for i in range(0, len(x) - 1))) \
    .reduceByKey(lambda a, b: a + b)

# Save output
bicounts.saveAsTextFile("hdfs://localhost:9000/output3")

# Download output
# $HADOOP_HOME/bin/hdfs dfs -cat /output3 /part-00000
# $HADOOP_HOME/bin/hdfs dfs -getmerge /output3 result3.txt
