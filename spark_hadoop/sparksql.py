"""This has to be run on PySpark Shell."""

from pyspark.sql import SparkSession

flightPerf = spark.read.csv(
    "/home/ubuntu/spark-2.2.0/downloads/lab5/departuredelays.csv",
    header='true',
    inferSchema='true'
)
flightPerf.createOrReplaceTempView("flightPerf")

airports = spark.read.csv(
    "/home/ubuntu/spark-2.2.0/downloads/lab5/airport-codes-na.csv",
    header='true',
    inferSchema='true'
)
airports.createOrReplaceTempView("airports")

spark.sql(
    "SELECT a.City, f.origin, SUM(f.delay) Delays \
    FROM flightPerf f JOIN airports a ON a.IATA = f.origin \
    GROUP BY a.City, f.origin ORDER BY SUM(f.delay) DESC \
    LIMIT 5"
).show()
