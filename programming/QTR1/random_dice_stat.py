"""
Monte Carlo Method
    An algorithm that uses a source of (pseudo) random numbers.
    Repeats an experiment many times and calculates a statistic, often an average.
    Estimates a value (often a probability) that is usually hard or impossible to calculate analytically.

Dice Statistics Problem
    Throw a pair of dice numbers of times and record what happens.
    More throws, more accurate estimate.
"""
from random import randint


def roll():
    return randint(1, 6)


def dice_stat(trials):
    count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count_prob = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(trials):
        val1 = roll()
        val2 = roll()
        dice_idx = val1 + val2 - 2
        count_list[dice_idx] = count_list[dice_idx] + 1
    for j in range(0, 11):
        count_prob[j] = count_list[j] / trials
        print("The probability for {j}: {p}".format(j=j + 2, p=count_prob[j]))
