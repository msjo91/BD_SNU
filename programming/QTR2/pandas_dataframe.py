import pandas as pd

sales_stats = {
    'Day': [1, 2, 3, 4, 5, 6],
    'Visitors': [43, 45, 33, 43, 78, 44],
    'Revenue': [64, 73, 62, 64, 53, 66]
}

df1 = pd.DataFrame(sales_stats)
print(df1)

# Location: Get from the first row to the row with index value 3
print(df1.loc[:3])  # Note!! The row 3 (fourth row) shows up as well!
# Index Location: Get row 0 to 2
print(df1.iloc[:3])

# Set index
df1 = df1.set_index('Day')
print(df1)

# Create data frame while setting index
df2 = pd.DataFrame(sales_stats, index=['a', 'b', 'c', 'd', 'e', 'f'])
print(df2)
print(df2.loc['c':'e'])
print(df2.iloc[1:4])

# Condition
print(df2[df2['Revenue'] > 65])
print(df2[(df2['Revenue'] > 65) | (df2['Visitors'] > 70)])

# Access column
print(df2['Visitors'])
print(df2[['Visitors', 'Revenue']])

# Change column order
print(pd.DataFrame(df2, columns=['Revenue', 'Visitors']))

# Add column
df3 = pd.DataFrame(df2, columns=['Visitors', 'Revenue', 'Debt'])  # The new column 'Debt' has only NaN value.
print(df3)

# Delete column
del df3['Debt']
print(df3)
print(df3.drop('Revenue', axis=1))  # Note!! The original df3 is untouched. Must assign a variable.

# Add row
df3.loc['g'] = [200, 77]
print(df3)

# Delete row
print(df3.drop('g', axis=0))  # Note!! The original df3 is untouched. Must assign a variable.

ddata = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df4 = pd.DataFrame(ddata)
print(df4)

# Rename columns
newcols = {'A': 'col_1', 'B': 'col_2', 'C': 'col_3'}
print(df4.rename(columns=newcols))  # Note!! The original df3 is untouched. Must assign a variable.

# Rename index
print(df4.rename(index={1: 'a'}))  # Note!! The original df3 is untouched. Must assign a variable.
