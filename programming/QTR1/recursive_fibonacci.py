def fib_recur(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)


def fib_iter(n):
    x = 0
    next_x = 1
    for i in range(1, n + 1):
        x, next_x = next_x, x + next_x
    return x
