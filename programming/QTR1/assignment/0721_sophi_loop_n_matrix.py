def m1(n):
    """Print a triangle of numbers."""
    for i in range(1, n + 1):
        print(*list(range(1, i + 1)), sep=' ')


def m2(n):
    """Print a triangle of consecutive numbers."""
    for i in range(1, n + 1):
        print(*list(range(int(1 + (i - 1) * i / 2), int(1 + i * (i + 1) / 2))), sep=' ')


def m3(n):
    """Print a triangle that ascends then decends."""
    for i in range(1, n + 1):
        print(*list(range(int(1 + i * (i - 1) / 2), int(1 + i * (i - 1) / 2 + i))), sep=' ')
    for i in range(n - 1, 0, -1):
        print(*list(range(int(1 + i * (i - 1) / 2), int(1 + i * (i - 1) / 2 + i))), sep=' ')


def m4(n):
    """Print a triangle of consecutive numbers that ascends then descends."""
    for i in range(1, n + 1):
        print(*list(range(int(1 + i * (i - 1) / 2), int(1 + i * (i - 1) / 2 + i))), sep=' ')
    for i in range(n - 1, 0, -1):
        print(*list(range(int(n * n - i * (i - 1) / 2 - i + 1), int(n * n - i * (i - 1) / 2 + 1))), sep=' ')


def m5(matrix):
    """Print the sum of every row in a matrix."""
    print(*list(map(lambda x: sum(x), matrix)), sep='\n')


def m6(matrix):
    """Return the sum of all the elements in the matrix."""
    return sum(map(lambda x: sum(x), matrix))


def m7(matrix):
    """Return the product of all the elements in a matrix."""
    from functools import reduce
    prod = 1
    for row in matrix:
        prod *= reduce(lambda x, y: x * y, row)
    print(prod)


def m8(matrix):
    """Print the odd numbers in the matrix with each row on one line."""
    for i in matrix:
        print(*list(filter(lambda x: x % 2 == 1, i)))


def m9(matrix1, matrix2):
    """Return the sum of matrix1 and matrix2."""
    return [list(map(lambda x: x[0] + x[1], zip(matrix1[row], matrix2[row]))) for row in range(len(matrix1))]


def m10(matrix1, matrix2):
    """Return the product of matrix1 and matrix2."""
    return [
        [sum([matrix1[i][k] * matrix2[k][j] for k in range(0, len(matrix1[0]))])
         for j in range(0, len(matrix2[0]))]
        for i in range(0, len(matrix1))
    ]


def m11(matrix):
    """Return True if the matrix is the identity matrix, and False otherwise."""
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row == col and matrix[row][col] != 1:
                return False
            if row != col and matrix[row][col] != 0:
                return False
    return True


def f12(rows, cols):
    """Return a two dimensional list where each element corresponds to how many adjacent neighbors it has."""
    return [
        [(row - 1 in range(rows)) + (row + 1 in range(rows)) + (col - 1 in range(cols)) + (col + 1 in range(cols))
         for col in range(cols)]
        for row in range(rows)
    ]
