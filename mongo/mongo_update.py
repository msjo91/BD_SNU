from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db = client.bde4
    collection = db.people
    collection.update({"name": "Lee"}, {"$set": {"name": "Lim", "age": 25}})
    collection.update({"name": "Kim"}, {"$set": {"age": 20}})
    collection.update({"name": "Park"}, {"$unset": {"skills": ""}})
    collection.update({"name": "Choi"}, {"$inc": {"score": -2}})
    cursor = collection.find()
    for doc in cursor:
        print(doc)
    client.close()


if __name__ == "__main__":
    main()
