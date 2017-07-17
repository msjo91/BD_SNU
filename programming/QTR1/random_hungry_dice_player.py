"""
Monte Carlo Method
    An algorithm that uses a source of (pseudo) random numbers.
    Repeats an experiment many times and calculates a statistic, often an average.
    Estimates a value (often a probability) that is usually hard or impossible to calculate analytically.

The Hungry Dice Player Problem
    Can I expect to make enough money playing it to buy lunch?
    That is, what is the expected (average) value won in the game?
"""
from random import randint


def roll():
    return randint(1, 6)


def dice_game():
    strikes = 0
    wins = 0
    while strikes < 3:  # 3 strikes then out
        die1 = roll()
        die2 = roll()
        if die1 == die2:
            strikes += 1
        else:
            wins += die1 + die2
    return wins  # in cents


def avg_wins(runs):
    """
    runs is the number of experiments to run
    """
    total = 0
    for n in range(runs):
        total += dice_game()
    return total / runs


def hungry_dice_player(runs):
    lst = []
    for i in range(5):
        lst.append(round(avg_wins(runs), 2))
    return lst
