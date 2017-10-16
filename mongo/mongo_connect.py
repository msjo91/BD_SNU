from pymongo import MongoClient


def main():
    client = MongoClient("localhost", 27017)
    db_list = client.database_names()
    print("DBs: {}".format(db_list))
    db_local = client['local']
    db_bde4 = client.bde4
    print("DB local: {}".format(db_local))
    print("DB bde4: {}".format(db_bde4))
    col_list = db_bde4.collection_names()
    col1 = db_bde4['apples']
    col2 = db_bde4.people
    print("bde4 Collections: {}".format(col_list))
    print("Collection 1: {}".format(col1))
    print("Collection 2: {}".format(col2))
    client.close()


if __name__ == "__main__":
    main()
