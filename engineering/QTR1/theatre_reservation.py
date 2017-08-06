import json
import os
import pymysql.cursors

# DB settings directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONF_DIR = os.path.join(BASE_DIR, ".conf")
CONFIG_FILE = os.path.join(CONF_DIR, "settings.json")
config = json.loads(open(CONFIG_FILE).read())

# Connect to DB
connection = pymysql.connect(
    host=config["db"]["host"],
    user=config["db"]["user"],
    password=config["db"]["password"],
    db=config["db"]["db"],
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True,
)


def act1():
    """
    Print all building info.
    """
    with connection.cursor() as c:
        sql = "select * from building"
        c.execute(sql)
        res = c.fetchall()
    print('%-5s %-20s %-10s %-10s %-15s %-10s' % (
        'id',
        'name',
        'location',
        'capacity',
        'assigned',
        'seat'
    ))
    for row in res:
        print('%-5d %-20s %-10s %-10d %-15d %-10d' % (
            row['id'],
            row['name'],
            row['location'],
            row['capacity'],
            row['assigned'],
            row['seat']
        ))


def act2():
    """
    Print all performance info.
    """
    with connection.cursor() as c:
        sql = "select * from performance"
        c.execute(sql)
        res = c.fetchall()
    print('%-5s %-20s %-10s %-10s %-10s' % (
        'id',
        'name',
        'type',
        'price',
        'booked'
    ))
    for row in res:
        print('%-5d %-20s %-10s %-10d %-10d' % (
            row['id'],
            row['name'],
            row['type'],
            row['price'],
            row['booked']
        ))


def act3():
    """
    Print all audience info.
    """
    with connection.cursor() as c:
        sql = "select * from audience"
        c.execute(sql)
        res = c.fetchall()
    print('%-5s %-20s %-10s %-10s' % (
        'id',
        'name',
        'gender',
        'age'
    ))
    for row in res:
        print('%-5d %-20s %-10s %-10d' % (
            row['aud_id'],
            row['name'],
            row['gender'],
            row['age']
        ))


def act4():
    """
    Add a new building in DB.
    """
    name = input("Building name: ")
    location = input("Building location: ")
    capacity = int(input("Building capacity: "))
    seat = int(input("Seat capacity: "))
    with connection.cursor() as c:
        sql = "insert into building (name, location, capacity, seat) values ('%s', '%s', %d, %d)" % (
            name,
            location,
            capacity,
            seat
        )
        c.execute(sql)


def act5():
    """
    Remove a building from DB.
    """
    building = input("Building id: ")
    with connection.cursor() as c:
        sql = "select id from building where id=%s" % building
        c.execute(sql)
        res = c.fetchall()
        if res is ():
            print("The building ID is not registered. Please check again.")
        sql = "delete from building where id=%s" % building
        c.execute(sql)


def act6():
    """
    Add a new performance in DB.
    """
    name = input("Performance name: ")
    genre = input("Performance type: ")
    price = int(input("Performance capacity: "))
    with connection.cursor() as c:
        sql = "insert into performance (name, type, price) values ('%s', '%s', %d)" % (
            name,
            genre,
            price
        )
        c.execute(sql)


def act7():
    """
    Remove a performance from DB.
    """
    performance = input("Performance id: ")
    with connection.cursor() as c:
        sql = "select id from performance where id=%s" % performance
        c.execute(sql)
        res = c.fetchall()
        if res is ():
            print("The performance ID is not registered. Please check again.")
        sql = "delete from performance where id=%s" % performance
        c.execute(sql)


def act8():
    """
    Add a new audience in DB.
    """
    name = input("Audience name: ")
    gender = input("Audience gender: ")
    age = int(input("Audience age: "))
    with connection.cursor() as c:
        sql = "insert into audience (name, gender, age) values ('%s', '%s', %d)" % (name, gender, age)
        c.execute(sql)


def act9():
    """
    Remove an audience from DB.
    """
    audience = input("Audience id: ")
    with connection.cursor() as c:
        sql = "select aud_id from audience where aud_id=%s" % audience
        c.execute(sql)
        res = c.fetchall()
        if res is ():
            print("The audience ID is not registered. Please check again.")
        sql = "delete from audience where aud_id=%s" % audience
        c.execute(sql)


def act10():
    """
    Assign a performance to a building.
    """
    building = input("Building ID: ")
    performance = input("Performance ID: ")
    with connection.cursor() as c:
        sql = "select performance_id from assign where assign.performance_id=%s" % performance
        c.execute(sql)
        res = c.fetchall()
        if res is not ():
            if int(res[0]['performance_id']) == int(performance):
                print("The performance has already been assigned.")
        else:
            sql = "select assigned from building where id=%s" % building
            c.execute(sql)
            res1 = c.fetchall()
            sql = "select capacity from building where id=%s" % building
            c.execute(sql)
            res2 = c.fetchall()
            if res1[0]['assigned'] >= res2[0]['capacity']:
                print("The building's assignments have reached full capacity. Cannot assign the performance.")
            else:
                sql1 = "insert into assign (building_id, performance_id) values (%s, %s)" % (
                    building,
                    performance
                )
                sql2 = "update building set assigned=assigned+1 where id=%s" % building
                c.execute(sql1)
                c.execute(sql2)
                print("Successfully assigned.")


def act11():
    """
    Book one or more performances.
    """
    performance = input("Performance ID: ")
    audience = input("Audience ID: ")
    seatnum = input("Seat number: ")
    seatlist = seatnum.split(',')
    try:
        with connection.cursor() as c:
            sql = "select seat from building, assign where assign.building_id=id and performance_id=%s" % performance
            c.execute(sql)
            res = c.fetchall()
            for seat in seatlist:
                try:
                    if int(seat) >= int(res[0]['seat']):
                        print("The seat is unavailable.")
                        break
                    else:
                        sql1 = "insert into seat (performance_id, audience_id, seat_number) values (%s, %s, %s)" % (
                            performance,
                            audience,
                            seat
                        )
                        sql2 = "update performance set booked=booked+1 where id=%s" % performance
                        c.execute(sql1)
                        c.execute(sql2)
                        print("Successfully booked seat {}".format(seat))
                except IndexError:
                    print("The performance is not assigned. Please check again.")
                    break
    except pymysql.Error:
        print("The seat is unavailable.")


def act12():
    """
    Print all assigned performances to a specific building.
    """
    building = int(input("Building ID: "))
    with connection.cursor() as c:
        sql = "select id from building"
        c.execute(sql)
        res1 = c.fetchall()
        for i in range(len(res1)):
            if res1[i]['id'] == int(building):
                sql = "select performance.id,performance.name,type,price,booked\
                 from assign,performance\
                  where assign.building_id=%s and assign.performance_id=performance.id" % building
                c.execute(sql)
                res2 = c.fetchall()
                if res2 is not ():
                    print('%-5s %-15s %-10s %-5s %-10s' % ('id', 'name', 'type', 'price', 'booked'))
                    for row in res2:
                        print('%-5d %-15s %-10s %-5s %-10d' % (
                            row['id'],
                            row['name'],
                            row['type'],
                            row['price'],
                            row['booked']
                        ))
                else:
                    print("No performance is assigned.")
                break
        sql = "select id from building where id=%s" % building
        c.execute(sql)
        res = c.fetchall()
        if res is ():
            print("The building ID is not registered. Please check again.")


def act13():
    """
    Print all audiences who booked a specific performance.
    """
    performance = int(input("Performance ID: "))
    with connection.cursor() as c:
        sql = "select id from performance"
        c.execute(sql)
        res1 = c.fetchall()
        for i in range(len(res1)):
            if res1[i]['id'] != int(performance):
                print("The performance ID is not registered. Please check again.")
                break
            else:
                sql = "select distinct aud_id, audience.name, gender, age from audience, seat\
                 where seat.audience_id=aud_id and seat.performance_id=%s" % performance
                c.execute(sql)
                res2 = c.fetchall()
                print('%-5s %-15s %-10s %-5s' % ('id', 'name', 'gender', 'age'))
                for row in res2:
                    print('%-5d %-15s %-10s %-5d' % (
                        row['aud_id'],
                        row['name'],
                        row['gender'],
                        row['age']
                    ))
            break


def act14():
    """
    Print the availability status of all seats.
    """
    performance = input("Performance ID: ")
    with connection.cursor() as c:
        sql = "select id from performance where id=%s" % performance
        c.execute(sql)
        res = c.fetchall()
        if res is ():
            print("The performance ID is not registered. Please check again.")
        else:
            sql = "select id from performance"
            c.execute(sql)
            res = c.fetchall()
            for i in range(len(res)):
                sql = "select performance_id from assign where assign.performance_id=%s" % performance
                c.execute(sql)
                result = c.fetchall()
                if result is ():
                    print("The performance is not assigned. Please check again.")
                    break
                else:
                    sql1 = "select seat_number, audience_id from seat where performance_id=%s" % performance
                    c.execute(sql1)
                    result1 = c.fetchall()
                    li = []
                    sql2 = 'select seat from building, assign\
                     where assign.building_id=id and assign.performance_id=%s' % performance
                    c.execute(sql2)
                    result2 = c.fetchall()
                    print(result2)
                    print('%-15s %-15s' % ('seat_number', 'audience_id'))
                    for j in range(1, result2[0]['seat'] + 1):
                        li.append([j, ''])
                    for row in result1:
                        li[row['seat_number'] - 1] = [row['seat_number'], row['audience_id']]
                    for k in li:
                        print('%-15s %-15s' % (k[0], k[1]))
                    break


def disconnect():
    connection.close()
    print("Good Bye! Have a great day!")


print("""
==============================================================
1. print all buildings
2. print all performances
3. print all audiences
4. insert a new building
5. remove a building
6. insert a new performance
7. remove a performance
8. insert a new audience
9. remove an audience
10. assign a performance to a building
11. book a performance
12. print all performances which assigned at a building
13. print all audiences who booked for a performance
14. print ticket booking status of a performance
15. exit
==============================================================
""")

while 1:
    action = int(input("Select your action: "))
    if action == 15:
        disconnect()
        break
    exec('act%d()' % action)
