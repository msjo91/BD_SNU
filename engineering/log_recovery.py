import json
import os
import re
import pymysql.cursors

# DB settings directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONF_DIR = os.path.join(BASE_DIR, ".conf")
CONFIG_FILE = os.path.join(CONF_DIR, "settings.json")
config = json.loads(open(CONFIG_FILE).read())

conn = 0  # Working connection
redo = []  # List of {tran: opers} to be done


def connect_db():
    """
    Connect to MySQL DB.
    """
    global conn

    conn = pymysql.connect(
        host=config["db"]["host"],
        user=config["db"]["user"],
        password=config["db"]["password"],
        db=config["db"]["db"],
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


def parse_log():
    """
    Read log file, then parse.
    """

    # Read log file
    logs = []
    with open('recovery.log', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            if '\n' in i:
                logs.append(i.replace('\n', ''))
            else:
                logs.append(i)

    # Parse log file
    global redo
    undo = []  # List of transactions to be undone

    # Fill undo list with transactions
    for log in logs:
        tran = log.split()[0]
        oper = log.split()[1]
        if log.startswith('checkpoint'):
            trans = log[11:].split(", ")
            undo.extend(trans)
        elif oper == 'start':
            undo.append(tran)
        elif oper == 'commit' or oper == 'abort':
            if tran in undo:
                undo.remove(tran)

    # Fill redo list with operations
    for log in logs:
        if len(log.split()) > 2:
            tran = log.split()[0]
            if tran in undo:
                li = re.sub(r'<T\d+> ', '', log).split(", ")
                opers = li[0].split(".") + li[1:]
                redo.append(opers)


def get_primary(li):
    """
    Get primary key field.
    """
    with conn.cursor() as c:
        sql = "SHOW COLUMNS FROM {}".format(li[0])
        c.execute(sql)
        res = c.fetchone()
    return res['Field']


def execute_recovery():
    """
    Reverse redo operations to recover records pre-transaction.
    """
    with conn.cursor() as c:
        for i in reversed(redo):
            sql = "UPDATE {tab} SET {col} = '{val1}' WHERE {key} = '{val2}'".format(
                tab=i[0],
                col=i[2],
                val1=i[-2],
                key=get_primary(i),
                val2=i[1]
            )
            c.execute(sql)


def disconnect_db():
    """
    Disconnect from MySQL DB.
    """
    conn.close()


def recover():
    connect_db()
    parse_log()
    execute_recovery()
    disconnect_db()


recover()
