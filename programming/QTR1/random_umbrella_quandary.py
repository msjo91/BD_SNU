from random import random


def umbrella(p):  # p is probability to rain
    """
    Person X walks between home and work every day and keeps an umbrella at each location.
    But he always forgets to carry one if it's not raining.
    If the probability to rain is p how many trips can he expect to make before he gets caught in the rain?
    """
    wet = False
    trips = 0
    location = 0
    umbrellas = [1, 1]  # index 0 stands for home, 1 stands for work
    while not wet:
        if random() < p:  # it's raining
            if umbrellas[location] == 0:  # no umbrella
                wet = True
            else:
                trips += 1
                umbrellas[location] -= 1  # take an umbrella
                location = 1 - location  # switch locations
                umbrellas[location] += 1  # put umbrella
        else:  # it's not raining; leave umbrellas where they are
            trips += 1
            location = 1 - location
    return trips


def test():
    """
    10000 experiments for each probability from 0.01 to 0.99.
    """
    results = [None] * 99
    p = 0.01
    for i in range(99):
        trips = 0
        for k in range(10000):
            trips += umbrella(p)
        results[i] = trips / 10000
        p += 0.01
    return results


def test_result():
    """Accumulate averages in a list."""
    res_list = test()
    for i in range(1, 100):
        print("The number of dry trips under the probability {p}%: {r}".format(p=i, r=res_list[i - 1]))
