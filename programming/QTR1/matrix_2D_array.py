# Find the sum of all elements in a 2D array (or matrix).
# Below variable "table" is a 3x4 matrix (3 rows, 4 columns).
table = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]


def sum_matrix(table):
    res = 0
    for row in range(len(table)):
        for col in range(len(table[row])):
            res += table[row][col]
    return res


# Access a whole row.
def access_row(table, row):
    row_list = table[row]
    return row_list


# Access a whole column.
def acess_column(table, col):
    col_list = []
    for row in range(len(table)):
        col_list += [table[row][col]]
        return col_list
