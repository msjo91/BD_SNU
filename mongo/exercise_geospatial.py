"""
From California, to Florida, to NYC Central Park.
Find the shortest straight distance between airports.
"""
from math import sqrt

from pymongo import MongoClient, GEOSPHERE

client = MongoClient('localhost', 27017)
db = client.bde4
airports = db.airports
states = db.states


def euclidean(f, t):
    """
    Calculate Euclidean Distance
    sqrt((x2 - x1)^2 + (y2 - y1)^x)
    """
    x = t['loc']['coordinates'][0] - f['loc']['coordinates'][0]
    y = t['loc']['coordinates'][1] - f['loc']['coordinates'][1]
    return sqrt(x ** 2 + y ** 2)


def eucli_min(dic):
    """
    Receive a dictionary and find the min value and it's key
    """
    key = min(dic, key=dic.get)
    return key, dic[key]


# Create 2dsphere index
airports.create_index([("loc", GEOSPHERE)])

# Coordinates
home = {'loc': {'type': 'Point', 'coordinates': [-119.125324, 36.312341]}}
cali = states.find_one({'code': 'CA'}, {'_id': 0, 'loc': 1})['loc']
flo = states.find_one({'code': 'FL'}, {'_id': 0, 'loc': 1})['loc']
cp = {'loc': {'type': 'Point', 'coordinates': [-73.96535, 40.782865]}}

# Airports (location, name, code)
cursor = airports.find(
    {'loc': {'$near': {'$geometry': home['loc']}},
     'loc.coordinates': {'$geoWithin': {'$geometry': cali}}},
    {'_id': 0, 'name': 1, 'code': 1, 'loc': 1}
)
c_air = [doc for doc in cursor]  # c_air is sorted by closeness to home
cursor = airports.find(
    {'loc.coordinates': {'$geoWithin': {'$geometry': flo}}},
    {'_id': 0, 'name': 1, 'code': 1, 'loc': 1}
)
f_air = [doc for doc in cursor]
cursor = airports.find(
    {'loc': {'$near': {'$geometry': cp['loc'], '$minDistance': 10000, '$maxDistance': 30000}}},
    {'_id': 0, 'name': 1, 'code': 1, 'loc': 1}
)
n_air = [doc for doc in cursor]

# Create a dictionary of Euclidean distance from home to Central Park.
d = {}
for c in c_air:
    e1 = euclidean(home, c)
    for f in f_air:
        e2 = euclidean(c_air[0], f)
        for n in n_air:
            e3 = euclidean(f, n)
            e4 = euclidean(n, cp)
            d[(c['code'], f['code'], n['code'])] = e1 + e2 + e3 + e4

res = eucli_min(d)
print(res)

# Remove index
airports.drop_index([("loc", GEOSPHERE)])
