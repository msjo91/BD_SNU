"""
Divide and Conquer
"""


def loop_power(a, n):
    ans = 1
    for i in range(n):
        ans *= a
    return ans


def recursive_power(a, n):
    # Raises a to the int power n
    if n == 0:
        return 1
    else:
        factor = recursive_power(a, n / 2)
        if n % 2 == 0:  # n is even
            return factor * factor
        else:  # n is odd
            return factor * factor * a
