def f1(n):
    """Print a triangle that grows upto the input number."""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j < i:
                print(j, end=' ')
            else:
                print(j, end='')
        print()


def f2(n):
    """Print a triangle that is consisted of ascending numbers."""
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 1
        print()


def f3(n):
    """Print a triangle that is consisted of ascending then descending numbers."""
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 1
        print()
    for i in range(n - 1):
        num -= 2 * (n - i - 1) + 1
        for j in range(n - i - 1):
            print(num, end=' ')
            num += 1
        print()


def f4(n):
    """Print a triangle consisted of ascending numbers."""
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 1
        print()
    for i in range(n - 1):
        for j in range(n - i - 1):
            print(num, end=' ')
            num += 1
        print()


def f5(matrix):
    """Print the sum of each row of the matrix."""
    for row in range(len(matrix)):
        ans = 0
        for col in range(len(matrix[0])):
            ans += matrix[row][col]
        print(ans)


def f6(matrix):
    """Print the diagonals of a matrix."""
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                print(matrix[row][col])


def f7(matrix):
    """Print the sum of every row in the matrix."""
    for row in range(len(matrix)):
        ans = 0
        for col in range(len(matrix[0])):
            ans += matrix[row][col]
        print(ans)


def f8(matrix):
    """Return the sum of all the elements in the matrix."""
    ans = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            ans += matrix[row][col]
    return ans


def f9(matrix):
    """Return the product of all the elements in a matrix."""
    ans = 1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            ans *= matrix[row][col]
    return ans


def f10(matrix):
    """Print the odd numbers in a matrix with each row on one line."""
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] % 2 == 1:
                print(matrix[row][col], end=' ')
        print()


def f11_a(matrix1, matrix2):
    """Return the sum of matrix1 and matrix2."""
    new_mat = []
    for row in range(len(matrix1)):
        new_row = []
        for col in range(len(matrix1[0])):
            ans = matrix1[row][col] + matrix2[row][col]
            new_row.append(ans)
        new_mat.append(new_row)
    return new_mat


def f11_b(matrix1, matrix2):
    """Return the sum of matrix1 and matrix2."""
    for row in range(len(matrix1)):
        for col in range(len(matrix1[0])):
            matrix1[row][col] += matrix2[row][col]
    return matrix1


def f12(matrix1, matrix2):
    """Return the product of matrix1 and matrix 2."""
    new_mat = []
    for row1 in range(len(matrix1)):
        new_row = []
        for col in range(len(matrix2[0])):
            ans = 0
            for row2 in range(len(matrix2)):
                ans += matrix1[row1][row2] * matrix2[row2][col]
            new_row.append(ans)
        new_mat.append(new_row)
    return new_mat


def f13(matrix):
    """Return True if matrix is the identity matrix, and False otherwise."""
    if len(matrix) == len(matrix[0]):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == col:
                    if matrix[row][col] != 1:
                        return False
                else:
                    if matrix[row][col] != 0:
                        return False
        return True
    else:
        return False


def f14_a(rows, cols):
    """Return a two dimensional list where each element corresponds to how many adjacent neighbors it has."""
    new_mat = []
    if rows == 1 and cols == 1:
        new_mat = [[0]]
    elif rows == 1 and cols == 2:
        new_mat = [[1, 1]]
    elif rows == 2 and cols == 1:
        new_mat = [[1], [1]]
    else:
        for row in range(rows):
            new_mat += [[0] * cols]
        for row in range(rows):
            for col in range(cols):
                if (row == 0 and (col == 0 or col == cols - 1)) or (row == rows - 1 and (col == 0 or col == cols - 1)):
                    new_mat[row][col] = 2
                elif row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                    new_mat[row][col] = 3
                else:
                    new_mat[row][col] = 4
    return new_mat


def f14_b(rows, cols):
    """Return a two dimensional list where each element corresponds to how many adjacent neighbors it has."""
    new_mat = []
    for row in range(rows):
        new_mat += [[0] * cols]
    for row in range(rows):
        for col in range(cols):
            ans = 0
            if row - 1 in range(rows):
                ans += 1
            if row + 1 in range(rows):
                ans += 1
            if col - 1 in range(cols):
                ans += 1
            if col + 1 in range(cols):
                ans += 1
            new_mat[row][col] = ans
    return new_mat
