import numpy as np

a = np.array([2, 4, 3], float)

a.sum()
# 2.0 + 4.0 + 3.0 = 9.0
# np.sum(a)

# Get each sum of each column
np.sum(a, axis=0)
# a.sum(axis=0)

# Get each sum of each row
np.sum(a, axis=1)
# a.sum(axis=1)

a.prod()
# 2.0 * 4.0 * 3.0 = 24.0
# np.prod(a)

a.mean()
# (2.0 + 4.0 + 3.0) / 3 = 3.0
# np.mean(a)

a.var()
# np.var(a)

a.std()
# np.std(a)

np.median(a)
