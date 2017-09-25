import json
import os
from math import log

import pymysql
import re

# Directory for DB info
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


def tf(id, term):
    """
    Calculate Term Frequency (TF).
    Normalized term frequency of a term t in a document d.
    """
    # n(d) = number of terms in document d
    with conn.cursor() as c:
        sql = "SELECT text FROM wiki WHERE id = {}".format(id)
        c.execute(sql)
        txt = c.fetchone()
        txt_li = txt['text'].split()
        nd = len(txt_li)

    # n(d, t) = number of occurrence of term t in document d (ATF)
    ndt = 0
    for i in txt_li:
        if re.sub(r'[,.!?\'"]+', '', i).lower() == term:
            ndt += 1

    # TF(d, t) = log(1 + n(d, t) / n(d))
    return log(1 + ndt / nd)


def idf(term):
    """
    Calculate Inverse Document Frequency (IDF).
    """
    # n(t) = number of documents containing term t
    with conn.cursor() as c:
        sql = "SELECT COUNT(DISTINCT id) FROM wiki_invert WHERE term = '{}'".format(term)
        c.execute(sql)
        nt = c.fetchone()['COUNT(DISTINCT id)']
    # IDF(t) = 1 / n(t)
    return 1 / nt


def tf_idf(id, term):
    """
    Calculate TF-IDF.
    TF-IDF(d, t) = TF(d, t) * IDF(d, t) = TF(d, t) / n(t)
    """
    ti = tf(id, term) * idf(term)
    print("('{term}' in {id}) TF-IDF: {ti}".format(term=term, id=id, ti=ti))


tf_idf(41631770, 'also')
tf_idf(6688599, 'debut')
tf_idf(13794826, 'language')