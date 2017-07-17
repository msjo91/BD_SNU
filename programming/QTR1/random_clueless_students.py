"""
Monte Carlo Method:
    An algorithm that uses a source of (pseudo) random numbers.
    Repeats an experiment many times and calculates a statistic, often an average.
    Estimates a value (often a probability) that is usually hard or impossible to calculate analytically.

The Clueless Student Problem:
    A clueless student faced a pop quiz: a scrambled list of the 24 Presidents of the 19C and their terms in office.
    The object was to match the President with the term.
    If the student guesses a random one-to-one matching, how many matches will be right out of the 24, on average?
"""

from random import shuffle


def student(pairs, samples):
    """
    pairs: The number of pairs guessed.
    samples: The number of samples taken.
    """
    correct = 0
    match = list(range(pairs))
    for i in range(samples):
        shuffle(match)  # generate a guess
        for j in range(pairs):
            if match[j] == j:
                correct += 1
    return correct / samples
