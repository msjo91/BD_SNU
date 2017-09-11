import pandas as pd
import numpy as np

# List to series
s1 = pd.Series([1, 3, 5, np.NaN, 6, 8])  # NaN is "Not a Number". It is taken as a null value.
print(s1)

# Array to series
a = np.array([1, 3, 5, np.NaN, 6, 8])
s2 = pd.Series(a)
print(s2)

# Dictionary to series
d = {'a': 0., 'b': 1., 'c': 2.}
s3 = pd.Series(d)
print(s3)

# Integer value
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
s4 = pd.Series(sdata)
print(s4)

# Index list and matching with a dictionary
states = ['Texas', 'Oregon', 'California', 'Ohio']  # 'California' will not have a value.
s5 = pd.Series(sdata, index=states)  # The 'California' NaN changes all integer values to float.
print(s5)

# Find NaN or not NaN
print(pd.isnull(s5))
print(pd.notnull(s5))
