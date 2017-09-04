"""
The shape of operands must be the same.
Operation happens between two elements from each array at the same location.
Note: array is not list!
"""

import numpy as np

a = np.array([1, 2, 3], float)
b = np.array([5, 2, 6], float)

a + b
# array([6., 4., 9.])

a - b
# array([-4., 0., -3.])

a * b
# array([5., 4., 18.])

b / a
# array([5., 1., 2.])

a % b
# array(1., 0., 3.])

b ** a
# array([5., 4., 216.])

a * 2
# array([2, 4, 6])
