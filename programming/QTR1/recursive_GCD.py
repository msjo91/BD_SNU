# Greatest Common Denominator
def gcd_recur(x, y, depth=0):
    print(" " * depth, "gcd({x}, {y})".format(x=x, y=y))
    if y == 0:
        result = x
    else:
        result = gcd_recur(y, x % y, depth + 1)
    print(" " * depth, "-> {}".format(result))
    return result


def gcd_iter(x, y):
    """
    Assume x = 4, y = 6.
    1. old_x = 4, x = 6, y = 4
    2. old_x = 6, x = 4, y = 2
    3. old_x = 4, x = 2, y = 0
    Since there is nothing else to divide y, 2 must be the common denominator.
    """
    while y > 0:
        old_x = x
        x = y
        y = old_x % y
    return x
