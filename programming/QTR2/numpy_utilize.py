import numpy as np

# Create an array of size 10 filled with 0
z = np.zeros(10)

# Set fifth value to 1 from above array
z[4] = 1

# Create an array with values ranging from 10 to 49
r = np.random.randint(low=10, high=50, size=40)

# Create a 5 * 5 matrix with values ranging from 0 to 24
mat = np.random.randint(25, size=(5, 5))

# Create a 5 * 5 identity matrix
i = np.eye(5)

# Create an 5 * 5 array with random values and find the minimum and maximum value
a = np.random.rand(5, 5)
a.max()
a.min()

# Multiply a 4 * 3 matrix by a 3 * 2 matrix
m1 = np.ones((4, 3))
m2 = np.random.rand(3, 2)
prod = m1.dot(m2)

# Transpose above matrix
t = prod.transpose()

# Create two matrices ranging from 0 to 24 and 25 to 49
m3 = np.random.randint(25, size=(5, 5))
m4 = np.random.randint(low=25, high=50, size=(5, 5))

# Add above matrices
res = m3 + m4

# Subtract above matrices
sub = m3 - m4
