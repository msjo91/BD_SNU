from pymongo import MongoClient, GEOSPHERE

client = MongoClient('localhost', 27017)
db = client.bde4
airports = db.airports
states = db.states

# Create 2dsphere index
airports.create_index([("loc", GEOSPHERE)])

# Get index info
cursor = airports.index_information()
print('===== Airports Indices =====')
for doc in cursor:
    print(doc)

# Remove index
airports.drop_index([("loc", GEOSPHERE)])

# Find California coordinates
loc_dict = states.find_one({'code': 'CA'}, {'_id': 0, 'loc.coordinates': 1})
cali = loc_dict['loc']['coordinates']

# Find international airports in California
cursor = airports.find({
    'type': 'International',
    'loc.coordinates': {
        '$geoWithin': {
            '$geometry': {
                'type': 'MultiPolygon', 'coordinates': cali
            }
        }
    }
}, {'_id': 0, 'name': 1, 'type': 1, 'code': 1}).sort('name')

print('\n===== California International Airports =====')
for doc in cursor:
    print(doc)

# Find location of SFO California
loc_dict = airports.find_one({'code': 'SFO'}, {'_id': 0, 'loc.coordinates': 1})
sfo = loc_dict['loc']['coordinates']

# Find second most distance airport from SFO in California

airports.create_index([('loc', GEOSPHERE)])  # Create geospatial index to use $near

cursor = airports.find({
    'loc': {
        '$near': {
            '$geometry': {
                'type': 'Point', 'coordinates': sfo
            }
        }
    },
    'loc.coordinates': {
        '$geoWithin': {
            '$geometry': {
                'type': 'MultiPolygon', 'coordinates': cali
            }
        }
    }
}, {'_id': 0, 'name': 1, 'type': 1, 'code': 1})

# Append California airports from closest to farthest
airport_list = []
for doc in cursor:
    airport_list.append(doc)

print('\n===== Second Furthest Airport from SFO in California =====')
print(airport_list[-2])

airports.drop_index([("loc", GEOSPHERE)])  # Remove index

# Get adjacent states to California
cursor = states.find({
    'loc': {
        '$geoIntersects': {
            '$geometry': {
                'type': 'MultiPolygon', 'coordinates': cali
            }
        }
    },
    'code': {'$ne': 'CA'}
}, {'_id': 0, 'name': 1, 'code': 1})

print('\n===== Adjacent States to California =====')
for doc in cursor:
    print(doc)

# Find international airports near NYC Central Park

airports.create_index([('loc', GEOSPHERE)])  # Create geospatial index to use $near

cursor = airports.find({
    'type': 'International',
    'loc': {
        '$near': {
            '$geometry': {
                'type': 'Point', 'coordinates': [-73.96535, 40.782865]
            },
            '$maxDistance': 20000
        }
    }
}, {'_id': 0, 'name': 1, 'code': 1})

print('\n===== International Airports within 20km from Central Park NYC =====')
for doc in cursor:
    print(doc)

airports.drop_index([("loc", GEOSPHERE)])  # Remove index
