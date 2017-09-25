import json
import os

import pymysql
import re

# Directory to DB info
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONF_DIR = os.path.join(BASE_DIR, ".conf")
CONFIG_FILE = os.path.join(CONF_DIR, "settings.json")
config = json.loads(open(CONFIG_FILE).read())

# Connect to DB
conn = pymysql.connect(
    host=config["db"]["host"],
    user=config["db"]["user"],
    password=config["db"]["password"],
    db=config["db"]["db"],
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True,
)

# Create inverted index table
with conn.cursor() as c:
    sql = """DROP TABLE IF EXISTS wiki_invert CASCADE;
    CREATE TABLE wiki_invert (term VARCHAR(1000), id INT(11));"""
    c.execute(sql)

# Select original table
with conn.cursor() as c:
    sql = "SELECT * FROM wiki"
    c.execute(sql)
    wiki = c.fetchall()

wordlist = ['also', 'debut', 'language', 'two']  # List of words to be invert indexed
idlist = []  # List of IDs where words in wordlist are found
idxdict = {}  # Compliation

# Get words and its locations
for w in wordlist:
    for line in wiki:
        txt_li = line['text'].split()
        li = [re.sub(r'[,.!?\'"]+', '', i).lower() for i in txt_li]
        if w in li:
            if line['id'] not in idlist:
                idlist.append(line['id'])
    idxdict[w] = idlist
    idlist = []

# Insert values
with conn.cursor() as c:
    for w in wordlist:
        ids = idxdict[w]
        for id in ids:
            sql = "INSERT INTO wiki_invert VALUES ('{term}', {id})".format(term=w, id=id)
            c.execute(sql)
