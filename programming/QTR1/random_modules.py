from random import shuffle, sample, choice, randrange, randint, uniform, random

# [0, 1)
[random() for i in range(5)]

# a <= N <= b (N is float)
[uniform(0, 10) for i in range(5)]

# a <= N <= b (N is integer)
[randint(0, 10) for i in range(5)]

# Same as randint(0, 10)
[randrange(11) for i in range(5)]

# randrange(start, end, step)
[randrange(0, 101, 2) for i in range(5)]

colors = ['red', 'blue', 'green', 'gray', 'black']
# Pick one
[choice(colors) for i in range(5)]

# Pick two as a list
[sample(colors, 2) for i in range(3)]

# Switcharoo
shuffle(colors)
