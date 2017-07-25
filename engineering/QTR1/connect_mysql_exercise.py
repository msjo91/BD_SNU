import json
import os
import pymysql.cursors

# DB settings directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONF_DIR = os.path.join(BASE_DIR, ".conf")
CONFIG_FILE = os.path.join(CONF_DIR, "settings.json")
config = json.loads(open(CONFIG_FILE).read())


def e31():
    """Print all student name and SSN."""
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
            sql = "SELECT name 이름, resident_id 주민등록번호 FROM student"
            c.execute(sql)
            result = c.fetchall()
            print(result)
    finally:
        connection.close()


def e32():
    """Print the names and work years of professors employed later than '최성희'"""
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
            sql = "SELECT name 이름, (2017 - year_emp) 재직년수 FROM professor \
            WHERE year_emp > (SELECT year_emp FROM professor WHERE name='최성희')"
            c.execute(sql)
            result = c.fetchall()
            print(result)
    finally:
        connection.close()


def e33():
    """Get course title and grade when given student name as input."""
    # Connect to DB
    connection = pymysql.connect(
        host=config["db"]["host"],
        user=config["db"]["user"],
        password=config["db"]["password"],
        db=config["db"]["db"],
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )

    name = input("What is the student's name: ")
    try:
        with connection.cursor() as c:
            sql = "SELECT title 과목명, grade 성적 \
            FROM student natural join takes t join class c on t.class_id=c.class_id natural join course \
            WHERE name='{}'".format(name)
            c.execute(sql)
            result = c.fetchall()
            print(result)
    finally:
        connection.close()
