from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db = client.bde4

    collection = db['post']
    collection.drop()
    post = {"author": "Mann", "text": "Hello, world!"}
    collection.insert_one(post)
    cursor = collection.find()
    print("BDE4 POST:")
    for doc in cursor:
        print(doc)

    collection = db.people
    collection.drop()
    posts = [
        {"name": "Kim", "age": 21},
        {"name": "Lee", "age": 22},
        {"name": "Park", "age": 27, "skills": ['mongodb', 'python']},
        {"name": "Choi", "age": 22, "score": 10}
    ]
    collection.insert_many(posts)
    cursor = collection.find()
    print("BDE4 PEOPLE:")
    for doc in cursor:
        print(doc)
    client.close()


if __name__ == "__main__":
    main()
