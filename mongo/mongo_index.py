from pprint import pprint

import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['bde4']
collection = db['pokedex']

# Print executionStats
cursor = collection.find({'name': 'Wartortle'}).explain()['executionStats']
pprint(cursor)

# Create index for a field
collection.create_index('name')
print(collection.index_information())

# Print again with index
pprint(cursor)

# Create a compound index
collection.create_index([('id', pymongo.DESCENDING), ('name', pymongo.ASCENDING)])
print(collection.index_information())

# Drop all indexes
collection.drop_indexes()
print(collection.index_information())

# Close connection
client.close()
