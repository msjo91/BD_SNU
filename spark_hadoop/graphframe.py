"""
This requires to be run in pyspark shell.
Graphframes must be loaded as well.
${SPARK_HOME}/bin/pyspark --packages graphframes:graphframes:0.5.0-spark2.1-s_2.11
"""

from pyspark.sql import *
from graphframes import *

# Get airports dataset
airportsFilePath = "downloads/lab6/airports-codes-na.csv"
airports = spark.read.csv(airportsFilePath, header='true')
airports.createOrReplaceTempView("airportsNA")

# Get departure delays dataset
delaysFilePath = "downloads/lab6/departuredelays.csv"
delays = spark.read.csv(delaysFilePath, header='true')
delays.createOrReplaceTempView("departureDelays")

# Get all delayed airports both source and destination
subquery = "SELECT DISTINCT src AS iata FROM departureDelays UNION ALL SELECT DISTINCT dst AS iata FROM departureDelays"
query = "SELECT DISTINCT iata FROM (%s) a" % subquery
tripIATA = spark.sql(query)
tripIATA.createOrReplaceTempView("tripIATA")

# A new airports view with renamed columns
tripVertices = airports.withColumnRenamed("ID", "No").distinct()  # ID -> No
tripVertices = tripVertices.withColumnRenamed("IATA", "id").distinct()  # IATA -> id

# A new delays view with selected columns
tripEdges = delays.select("tripid", delays.delay.cast("int"), "src", "dst", "city_dst",
                          "state_dst")  # Make sure "delay" values are integers
tripEdges = tripEdges.withColumn("label", tripEdges["delay"].cast("int"))

# Create a graphframe
tripGraph = GraphFrame(tripVertices, tripEdges)

