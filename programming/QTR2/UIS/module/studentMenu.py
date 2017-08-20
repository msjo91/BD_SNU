from DBconnection import return_connect
from userAcc import user_acc


def student_menu():
    """Call student menu index."""
    menu_num = -1

    while menu_num != '0':
        print("\n\nWelcome %s" % user_acc.name)
        print("select student menu")
        print("1) Student Report")
        print("2) Check Course Qualification")
        print("3) View Time Table")
        print("0) Quit")
        menu_num = input("Enter: ")

        switcher = {
            '0': quit_menu,
            '1': print_stud_report,
            '2': print_course_qual,
            '3': print_time_table
        }

        selected_func = switcher.get(menu_num, print_wrong)
        selected_func()
    return


def print_stud_report():
    """Get student's grade report"""
    c = user_acc.conn.cursor()
    c.execute("SELECT * FROM student \
                WHERE ID = \"%s\" and name= \"%s\"" % (user_acc.id_, user_acc.name))
    data = c.fetchone()

    print("You are a member of %s" % data[2])
    print("You have taken total %s credits\n" % data[3])
    print("Semester report\n")

    # GPA
    # Get years and semesters
    sql = "SELECT DISTINCT year, semester FROM takes WHERE ID={} ORDER BY year, semester DESC".format(user_acc.id_)
    c.execute(sql)
    result1 = c.fetchall()

    # Get grades and credits
    for year, semester in result1:
        sql = "SELECT grade, credits FROM course NATURAL JOIN takes \
        WHERE ID={id} AND year={year} AND semester='{semester}'".format(
            id=user_acc.id_,
            year=year,
            semester=semester
        )
        c.execute(sql)
        result2 = c.fetchall()
        # Use zip (grade, credits)
        grade, credits = zip(*result2)
        gps = []
        for i in grade:
            gps.append(gp_to_float(i))

        # Print GPA
        print("\n%s\t%s\tGPA : %d" % (year, semester, sum(gps) / len(gps)))
        # Print grade for each course
        print("%10s\t%40s\t%15s\t%8s\t%8s" % ("course_id", "title", "dept_name", "credit", "grade"))

        # Get course_id, title, dept_name, credit, grade
        sql = "SELECT course_id, title, dept_name, credits, grade \
        FROM course NATURAL JOIN takes \
        WHERE ID={id} AND year={year} AND semester='{semester}'".format(
            id=user_acc.id_,
            year=year,
            semester=semester
        )
        c.execute(sql)
        result3 = c.fetchall()
        for course_id, title, dept_name, credit, grade in result3:
            print("%10s\t%40s\t%15s\t%8d\t%8s" % (course_id, title, dept_name, credit, grade))

    # Close
    c.close()


def print_course_qual():
    c = user_acc.conn.cursor()

    while True:
        print("\nCheck Course Qualification")
        course_info = input("Enter course ID or Title (Enter q to go back) : ")

        if course_info == "q" or course_info == "Q":
            break

            # Distinguish course_id and title
            sql = "SELECT course_id FROM course WHERE title='{}'".format(course_info)
            c.execute(sql)
            # If input is not course_id
            if not c.fetchall():
                sql = "SELECT title FROM course WHERE course_id={}".format(course_info)
                c.execute(sql)
                # If input is wrong
                if not c.fetchall():
                    print("Wrong input or the course is not registered.")
                    return
            # If input is course_id
            else:
                course_id = course_info
                title = c.fetchone()
        # If input is title
        else:
            course_id = c.fetchone()
            title = course_info
        # Get prereq_id
        sql = "SELECT prereq_id FROM prereq WHERE course_id={}".format(course_id)
        c.execute(sql)
        result = c.fetchall()
        # If prereq exists
        if result is True:
            prereq_id = str(*result[0]).split(",")
        # If prereq does not exist
        else:
            prereq_id = None

        # Check if the user has taken the pre-requsite courses
        sql = "SELECT ID, course_id FROM takes WHERE ID={} AND course_id"

        # 수강 조건 만족 표시




        # 수강 조건 불만족 표시




        # Show taken pre-requisite courses
        sql = "SELECT course_id, title, dept_name, credits FROM course WHERE course_id"
        c.execute(sql)
        result = c.fetchall()
        for course_id, title, dept_name, credit in result:
            print("%10d\t%40s\t%15s\t%8d" % (course_id, title, dept_name, credit))

    # Close
    c.close()
    return


def print_time_table():
    c = user_acc.conn.cursor()

    # Get year and semester
    sql = "SELECT DISTINCT year, semester FROM takes WHERE ID={}".format(user_acc.id_)
    c.execute(sql)
    result1 = c.fetchall()

    # Print time table
    print("\nTime Table\n")
    print("%10s\t%40s\t%15s\t%10s\t%10s" % ("course_id", "title", "day", "start_time", "end_time"))

    # Create time table
    for year, semester in result1:
        sql = "SELECT course.course_id, title, day, start_hr, start_min, end_hr, end_min \
        FROM course NATURAL JOIN takes NATURAL JOIN section NATURAL JOIN time_slot \
        WHERE ID={id} AND year={year} AND semester='{semester}'".format(
            id=user_acc.id_,
            year=year,
            semester=semester
        )
        c.execute(sql)
        result2 = c.fetchall()
        for course_id, title, day, start_hr, start_min, end_hr, end_min in result2:
            start_time = str(start_hr) + ":" + str(start_min)
            end_time = str(end_hr) + ":" + str(end_min)
            print("%10s\t%40s\t%15s\t%10s\t%10s" % (course_id, title, day, start_time, end_time))
    # Close
    c.close()
    return


def quit_menu():
    """Sign out."""
    global user_acc  # global 변수 write할 때는 명시 필요
    # Return connection
    return_connect(user_acc.conn)
    del user_acc
    return


def print_wrong():
    """When wrong menu number has been input."""
    print("\nWrong menu number.")
    return


def gp_to_float(grade):
    """Grade to GP."""
    return {
        "A+": 4.3,
        "A ": 4,
        "A-": 3.7,
        "B+": 3.3,
        "B ": 3,
        "B-": 2.7,
        "C+": 2.3,
        "C ": 2,
        "C-": 1.7,
        "D+": 1.3,
        "D ": 1,
        "D-": 0.7,
        "F": 0
    }[grade]
