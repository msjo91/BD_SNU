# Pseudo Code (= lingually expressed algorithm)
"""
Input: A number "n":
1. Create a list "numlist" with every integer from 2 to n, in order. (Assume n > 1)
2. create an empty list "primes".
3. For each element in "numlist":
    a. If element is not marked, copy it to the end of "primes".
    b. Mark every number that is a multiple of the most recently discovered prime number.
Output: List "primes" of all prime numbers less than or equal to "n"
"""
import math


def sift(li, k):
    """
    Filters out the multiples of the number k from list by marking them with the special value None.
    """
    i = 0
    while i < len(li):
        if li[i] is not None and li[i] % k == 0:
            li[i] = None
        i += 1
    return li


def sift2(li, k):
    """
    Filters out the multiples of the number k from list by modifying the list.
    """
    i = 0
    while i < len(li):
        if li[i] % k == 0:
            li.remove(li[i])
        else:
            i += 1
    return li


def sieve(n):
    """
    Use the first version of sift in this function, which does the filtering using None.
    """
    numlist = list(range(2, n + 1))
    primes = []
    for i in range(len(numlist)):
        if numlist[i] is not None:
            primes.append(numlist[i])
            sift(numlist, numlist[i])
    return primes


def better_sieve(n):
    numlist = list(range(2, n + 1))
    primes = []
    i = 0
    while i + 2 <= math.sqrt(n):
        if numlist[i] is not None:
            primes.append(numlist[i])
            sift(numlist, numlist[i])
        i += 1
    temp_list = []
    for i in range(len(numlist)):
        if numlist[i] is not None:
            temp_list.append(numlist[i])
    return primes + temp_list
