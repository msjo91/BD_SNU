import json
import os
import pymysql.cursors

# DB settings directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
CONF_DIR = os.path.join(ROOT_DIR, ".conf")
CONFIG_FILE = os.path.join(CONF_DIR, "settings.json")
config = json.loads(open(CONFIG_FILE).read())

# Connect to DB
connection = pymysql.connect(
    host=config["db"]["host"],
    user=config["db"]["user"],
    password=config["db"]["password"],
    db=config["db"]["db"],
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as c:
        # Select records from student table
        sql = "SELECT * FROM student"
        c.execute(sql)
        result = c.fetchall()
        print(result)
finally:
    connection.close()
