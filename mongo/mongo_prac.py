from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.bde4
collection = db.grade


def grader(lst):
    total = 0
    for i in lst:
        res = i.count('1')
        total += (res * (res + 1)) / 2
    return total


def reporter(directory):
    lst = []
    with open(directory) as f:
        lines = f.read().split('\n')[1:-1]
        for idx, line in enumerate(lines):
            d = {}
            nozero = map(str.strip, filter(str.strip, line.split('0')))
            d["sid"] = idx
            d["score"] = grader(nozero)
            lst.append(d)
    return lst


def creator(directory):
    collection.drop()
    posts = reporter(directory)
    collection.insert_many(posts)
    cursor = collection.find()
    print("Before:")
    for doc in cursor:
        print(doc)


def updater():
    collection.update_many({"score": 55.0}, {"$inc": {"score": 5}})
    collection.update({"sid": 5}, {"$inc": {"score": -1}})
    cursor = collection.find()
    print("After:")
    for doc in cursor:
        print(doc)


if __name__ == "__main__":
    creator("grade.txt")
    updater()
    client.close()
