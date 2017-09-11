import pandas as pd
import numpy as np

ddata = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 2D array
cols = ['A', 'B', 'C']
df = pd.DataFrame(data=ddata, columns=cols)
print(df)

# Can access each row using iterrows()
for idx, row in df.iterrows():
    print(row['A'], row['B'])
