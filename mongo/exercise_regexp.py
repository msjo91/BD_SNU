import re
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.bde4
collection = db.pokedex

# One way
cursor = collection.find({'spawn_time': {"$gte": "20", "$lte": "24"}},
                         {'_id': 0, 'id': 1, 'name': 1, 'spawn_time': 1}).sort('spawn_time')

# Using regexp
cursor = collection.find(
    {'spawn_time':
         {"$in":
              [re.compile('^20'), re.compile('^21'), re.compile('^22'), re.compile('^23'), '24:00']
          }
     },
    {'_id': 0, 'id': 1, 'name': 1, 'spawn_time': 1}
).sort('spawn_time')

for doc in cursor:
    print(doc)

client.close()
