def is_prime_dumb(n):
    if n < 2:
        return False
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True


def is_prime_better(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for factor in range(3, n, 2):  # Skips all multiples of 2
        if n % factor == 0:
            return False
    return True


def is_prime_best(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    max_factor = round(n ** 0.5)
    for factor in range(3, max_factor + 1, 2):
        if n % factor == 0:  # Reduces modulo compute number
            return False
    return True


def dumb_print(n):
    for i in range(n):
        if is_prime_dumb(i):
            print(i)
