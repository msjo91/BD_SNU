# Linear Congruential Generator (LCG)
def lcg_temp(a, n, c, m):
    """
    a, c, m are consonants.
    c and m are relatively prime (i.e. the only positivie interger that divides both c and m is 1).
    a - 1 is divisible by all prime factors of m.
    If m is a multiple of 4, so is a - 1.
    """
    return (a * n + c) % m


# Pseudo Random Number Generator (PRNG)
x = 0  # global internal state / seed


def prng_seed(s):  # seed the generator
    global x
    x = s


def lcg(n):  # LCG
    return (n + 7) % 12


def prng():  # state updater
    global x
    x = lcg(x)
    return x
