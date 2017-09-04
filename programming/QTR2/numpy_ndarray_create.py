import numpy as np

# np.array(list)
# Create an array while defining element type
a = np.array([1, 4, 5, 8], float)
# Create a multidimensional array
m = np.array([[1, 2, 3], [4, 5, 6]], float)
# If element type is not declared, string type can be input
str_a = np.array([1, 2, 3, 'four', 'five'])
# np.arange(start_num, end_num, interval)
# Create an array of sequential numbers
s = np.arange(10, 30, 5)

# np.zeros((row, col))
# Create a multidimensional array filled with 0s
# Default is float
z = np.zeros((2, 3))
# np.ones((row, col))
# Fill with 1s
# Default is float
o = np.ones((4, 2))
# np.full((row, col), val)
# Fill with given value
f = np.full((1, 3), 7)
# np.eye(size)
# Create an identity matrix
i = np.eye(4)

# np.random.rand(row, col)
# Fill with random numbers
r1 = np.random.rand(3, 3)
# np.random.random((row, col))
# Fill with random numbers between [0, 1)
r2 = np.random.random((2, 2))


def print_type(var):
    """All data types are numpy.ndarray."""
    print(type(var))
