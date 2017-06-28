"""
Euler's approach to the Basel Problem
(π ** 2) / 6 = ∑(1 / n ** 2)
π = (∑(1 / n ** 2) * 6) ** .5
"""


def pi_series_iter(n):
    result = 0
    for i in range(1, n + 1):
        result += 1 / (i ** 2)
    return result


def pi_approx_iter(n):
    x = pi_series_iter(n)
    return (6 * x) ** .5


def pi_series_recur(n):
    assert n >= 0  # If assert is True, continue. If assert is False, break.
    if n == 0:
        return 0  # base case
    else:
        return pi_series_recur(n - 1) + 1 / n ** 2  # recursive case


def pi_approx_recur(n):
    x = pi_series_recur(n)
    return (6 * x) ** .5
