# Create a variable-sized 2D array.
def create_2d_array(rows, cols):
    table = []
    for row in range(rows):
        table += [[0] * cols]
    return table


# Change element in a matrix.
def change_element(table, row, col, num):
    table[row][col] = num
    return table


# 2D arrays do not really exist in Python.
# They are lists that happen to contain other lists as elements.
# This can be done for "3D lists", or even "4D" or higher-dimensional lists.
# These can also be non-rectangular.
def create_3d_list(x, y, z):
    li = []
    for i in range(x):
        for j in range(y):
            li += [[[0] * z] * y]
    return li


print("Note: Rather use 'Array Module' or 'NumPy Module'")
