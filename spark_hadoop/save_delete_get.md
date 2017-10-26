#### Save in hadoop
Open spark-shell

```
<RDD>.saveAsTextFile("hdfs://localhost:9000/<name>")
```
####Download from hadoop
```
$HADOOP_HOME/bin/hdfs dfs -cat /path/in/hadoop /path/in/hadoop/<part>
$HADOOP_HOME/bin/hdfs dfs -getmerge /path/in/hadoop <name>.txt
```
#### Delete from hadoop
```
$HADOOP_HOME/bin/hdfs dfs -rm -r /path
```