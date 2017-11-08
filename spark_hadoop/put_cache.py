"""
This is an example PySpark script to demonstrate the use of .cache().
"""

import sys

import numpy as np

lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])  # "lines" is used only once. (No reason to cache)
data = lines.map(parseVector).cache()  # <-- Right Here!
kPoints = data.takeSample(False, K, 1)  # Not RDD dataset (Can't use .cache())
while tempDist > convergeDist:
    closest = data.map(lambda p: (
    closestPoint(p, kPoints), (p, 1)))  # Flexible RDD (.cache() is for frequent recalling of a solid RDD)
    pointStats = closest.reduceByKey(
        lambda p1_c1, p2_c2: (p1_c1[0] + p2_c2[0], p1_c1[1] + p2_c2[1])
    )  # Flexible RDD (.cache() is for frequent recalling of a solid RDD)
    newPoints = pointStats.map(
        lambda st: (st[0], st[1][0] / st[1][1])).collect()  # Not RDD dataset (Can't use .cache())
    tempDist = sum(np.sum((kPoints[iK] - p) ** 2) for (iK, p) in newPoints)
    for (iK, p) in newPoints:
        kPoints[iK] = p
