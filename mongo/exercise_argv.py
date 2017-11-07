import sys

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.bde4
collection = db.pokedex

# Get arguments and
weak = {}
for mon in sys.argv[1:]:
    cursor = collection.find_one({'name': mon})
    weak[mon] = cursor['weaknesses']

# Intersect common elements
cmn_weak = None
for key in (k for k in sys.argv[1:] if k in weak):
    if cmn_weak is None:
        cmn_weak = set(weak[key])
    else:
        cmn_weak &= set(weak[key])

# Find records with selected fields if field contains a certain element in sublist
cursor = collection.find({'type': {"$in": list(cmn_weak)}},
                         {'_id': 0, 'id': 1, 'name': 1, 'type': 1}).sort('name')

for doc in cursor:
    print(doc)

client.close()
