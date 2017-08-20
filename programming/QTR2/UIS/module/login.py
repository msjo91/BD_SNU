from DBconnection import get_connect, close_db
from instructorMenu import instructor_menu
from studentMenu import student_menu
from userAcc import user_acc


def auth(id_, name):
    """Authenticate user."""
    user_connect = get_connect()

    # Check if input ID and name exist in database.
    with user_connect.cursor() as c:
        sql = "SELECT * FROM \
        (SELECT ID, name FROM student UNION SELECT ID, name FROM instructor) sub \
        WHERE ID={id} AND name='{name}'".format(id=id_, name=name)
        c.execute(sql)
        result1 = c.fetchall()

        # Check if user is instructor.
        if result1:
            sql = "SELECT * FROM instructor WHERE ID={id} AND name='{name}'".format(id=id_, name=name)
            c.execute(sql)
            result2 = c.fetchall()

            if result2:
                return user_acc.set_attrs(id_=id_, name=name, role=1, conn=user_connect)
            else:
                return user_acc.set_attrs(id_=id_, name=name, role=0, conn=user_connect)

        else:
            print("{id} {name} does not exist. Please try again.".format(id=id_, name=name))
            return login()


def login():
    """Sign in."""
    while user_acc.conn is None:
        print("Please sign in")
        id_ = input("%-10s:" % "ID")
        name = input("%-10s:" % "Name")
        auth(id_, name)

        switcher = {
            0: student_menu,
            1: instructor_menu
        }

        role_menu = switcher.get(user_acc.role)
        role_menu()
