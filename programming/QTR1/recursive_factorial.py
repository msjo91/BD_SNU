"""
def recursive(x):
    do work
    if more work to do:
        recursive(next(x))
    return result

Note: next(x) should need less work than x.
      Base case is a case which recursion is not applied.
      All chains of recursion must end up at one of the base cases.

RecursionError: maximum recursion depth exceeded in comparison
    >> when the process is beyond computing ability
"""


# 0! = 1 (base case)
# n! = n * (n - 1)! (recursive case)
# n =< 1986 (recursion error)
def factorial_recur(n, depth=0):
    print(" " * depth, "factorial({})".format(n))
    if n < 2:
        result = 1
    else:
        result = n * factorial_recur(n - 1, depth + 1)
    print(" " * depth, "-> {}".format(result))
    return result


# Below version has no limit since it does not require stacks.
# No recursion error.
def factorial_iter(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
