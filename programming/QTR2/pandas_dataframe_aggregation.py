import pandas as pd
import numpy as np

ddata = {
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.rand(8)
}
df1 = pd.DataFrame(ddata)
print(df1)

# groupby
df2 = df1.groupby('A')
print(df2)  # This only prints that df2 is a DataFrameGroupBy object

# Aggregation
print(df2.mean())
print(df2.sum())
print(df2.get_group('bar'))  # Get only 'bar' group

df3 = df1.groupby(['A', 'B'])
print(df3.mean())
