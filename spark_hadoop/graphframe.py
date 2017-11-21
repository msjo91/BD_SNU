"""
This requires to be run in pyspark shell.
Graphframes must be loaded as well.
${SPARK_HOME}/bin/pyspark --packages graphframes:graphframes:0.5.0-spark2.1-s_2.11
"""

from pyspark.sql import *
from pyspark.sql import functions as F
from graphframes import *

# Get departure delays dataset
delaysFilePath = "downloads/lab6/departuredelays.csv"
delays = spark.read.csv(delaysFilePath, header='true')
delays.createOrReplaceTempView("departureDelays")

# Get all delayed airports both source and destination
subquery = "SELECT DISTINCT src AS iata FROM departureDelays UNION ALL SELECT DISTINCT dst AS iata FROM departureDelays"
query = "SELECT DISTINCT iata FROM (%s) a" % subquery
tripIATA = spark.sql(query)
tripIATA.createOrReplaceTempView("tripIATA")

# Get airports dataset
airportsFilePath = "downloads/lab6/airports-codes-na.csv"
airports = spark.read.csv(airportsFilePath, header='true')
airports.createOrReplaceTempView("airportsNA")

# Leave only airports which has delayed departures
query = "SELECT a.* FROM airportsNA a JOIN tripIATA t ON a.IATA = t.IATA"
delayports = spark.sql(query)

# A new airports view with renamed columns
tripVertices = delayports.withColumnRenamed("ID", "No").distinct()  # ID -> No
tripVertices = tripVertices.withColumnRenamed("IATA", "id").distinct()  # IATA -> id

# A new delays view with selected columns (Make sure "delay" values are intergers)
tripEdges = delays.select("tripid", delays.delay.cast("int"), "src", "dst", "city_dst", "state_dst")
tripEdges = tripEdges.withColumn("label", tripEdges["delay"].cast("int"))

# Create a graphframe
tripGraph = GraphFrame(tripVertices, tripEdges)

# The longest delay in dataset
maxDelay = tripGraph.edges.groupBy().max("delay")
li = maxDelay.select('max(delay)').collect()
val = li[0]['max(delay)']
query = "SELECT * FROM departureDelays WHERE delay = %d" % val
longestDelay = spark.sql(query)
longestDelay.show()

# The number of delayed versus on-time/eary flights
delay_count = tripGraph.edges.filter("delay > 0").count()
norm_count = tripGraph.edges.filter("delay <= 0").count()
print("Delayed flights: %d \tOn-time/early flights: %d" % (delay_count, norm_count))

# What flights departing Seattle(SEA) are most likely to have significant delays?
delaySEA = tripGraph.edges.filter("src = 'SEA' and delay > 0") \
    .groupBy("src", "dst").avg("delay").orderBy("avg(delay)", ascending=False)
delaySEA.show()

# Top 5 busiest airports (most flights in and out)
ins = tripGraph.inDegrees
ins.createOrReplaceTempView("Ins")
outs = tripGraph.outDegrees
outs.createOrReplaceTempView("Outs")
query = "SELECT i.id, inDegree, outDegree FROM Ins i JOIN Outs o ON i.id = o.id"
ins_n_outs = spark.sql(query)
total = ins_n_outs.groupBy('id').agg(F.sum(ins_n_outs.inDegree + ins_n_outs.outDegree))
total.orderBy('sum((inDegree + outDegree))', ascending=False).limit(5).show()

# Airport rankings by PageRank
ranks = tripGraph.pageRank(resetProbability=0.15, maxIter=5)
ranks.vertices.orderBy(ranks.vertices.pagerank.desc()).show()
