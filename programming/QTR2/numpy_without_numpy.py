from statistics import mean
from matplotlib.pyplot import plot
from sklearn.linear_model import LinearRegression

# Create a 4X4 matrix
data = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]


def sum_matrix(table):
    """Use a function to add every entry in the matrix."""
    sum = 0
    for row in range(len(table)):
        for col in range(len(table[row])):
            sum += table[row][col]
    return sum


# Get columns
X_data = [2, 6, 10]
Y_data = [3, 7, 11]

# Use Statistics module to get mean of a column
print(mean(X_data))

# Use Sklearn module to get a linear regression model of two columns
regr = LinearRegression()
regr.fit(X_data, Y_data)
regr

# Use Matplotlib module to plot
plot(X_data, Y_data)
