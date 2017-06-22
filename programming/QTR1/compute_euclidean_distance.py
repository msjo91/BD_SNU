# Euclidean Distance is the distance between two coordinates on an orthogonal coordinate system.
# For example, the distance between (x1, y1), (x2, y2) is
# math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
import math


def eucDist(n, p1, p2):
    """
    :param n: dimension
    :param p1: list with a length of n
    :param p2: list with a length of n
    :return: Euclidean Distance
    """
    distance = 0
    for i in range(n):
        distance += (p2[i] - p1[i]) ** 2
    return math.sqrt(distance)
