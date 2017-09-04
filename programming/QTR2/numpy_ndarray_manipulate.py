import numpy as np

# Slice
a = np.array([[1, 2, 3], [4, 5, 6]], float)
a[1:]
# array([[4., 5., 6.]])
a[1,:]
# array([4., 5., 6.])
a[:2]
# array([[1., 2., 3.], [4., 5., 6.]])
a[:,2]
# array([3., 6.])
a[-1:,-2:]
# array([[5., 6.]])

# Reshape
# Reshape an array to 2X3 matrix
mat = np.array(range(6), float).reshape((2, 3))

# Transpose
# Transpose a 2X3 matrix to a 3X2 matrix
mat.transpose()

# Flatten
# Turn multidimensional array into an 1D array
mat.flatten()

# Concatenate
a1 = np.array([1, 2], float)
a2 = np.array([3, 4, 5, 6], float)
a3 = np.array([7, 8, 9], float)
np.concatenate((a1, a2, a3))
