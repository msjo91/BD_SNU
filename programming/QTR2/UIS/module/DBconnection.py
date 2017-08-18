import os
import json
import MySQLdb

# DB settings directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONF_DIR = os.path.join(BASE_DIR, ".conf")
CONFIG_FILE = os.path.join(CONF_DIR, "settings.json")
config = json.loads(open(CONFIG_FILE).read())

# Create connection pool
connect_pool = []


def connect_db():
    """Create a connection to database."""
    connection = MySQLdb.connect(
        host=config["db"]["host"],
        user=config["db"]["user"],
        passwd=config["db"]["password"],
        db=config["db"]["db"],
        autocommit=True
    )
    return connection


def get_connect():
    """
    Pull connection from pool.
    Create and save a new connection in pool before if not existed.
    """
    global connect_pool
    if not connect_pool:
        connect_tmp = connect_db()
        connect_pool.append(connect_tmp)
    return connect_pool.pop()


def return_connect(conn):
    """Save connection in pool."""
    global connect_pool
    connect_pool.append(conn)
    return


def close_db(db):
    """Close connection."""
    return db.close()


def test_connection():
    """Test if connection is successful."""
    with connect_db().cursor() as c:
        c.execute("SELECT DATABASE(), CONNECTION_ID(), USER(), VERSION()")
        result = c.fetchall()
        print("Database: {db}\nConnection ID: {id}\nUser: {u}\nMySQL version: {v}".format(
            db=result[0][0],
            id=result[0][1],
            u=result[0][2],
            v=result[0][3]
        ))


# Choose functions to import when "from DBconnection import *"
__all__ = ['connect_db', 'get_connect', 'return_connect', 'close_db']
