import threading

x = 0


def inc():
    global x
    for i in range(1000000):
        x += 1


def dec():
    global x
    for i in range(1000000):
        x -= 1


t1 = threading.Thread(target=inc)
t2 = threading.Thread(target=dec)
# Due to interleaving, instructions of threads are performed one-by-one, "mixed".
# Note: A Thread object can be started ONLY ONCE!
t1.start()
t2.start()
t1.join()
t2.join()
# The end result is always different because these threads run independently.
print(x)


def countdown(count):
    """A countdown function with a parameter."""
    while count != 0:
        count -= 1
    return


# Input arguments
t3 = threading.Thread(target=countdown, args=(10,))
t3.start()
t3.join()
print(t3)

# Return the main Thread object. Usually, it is which the Python Interpreter was started.
print(threading.main_thread())
