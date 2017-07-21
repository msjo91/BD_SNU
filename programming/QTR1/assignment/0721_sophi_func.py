def f1(lst):
    """Return the number of odd elements in a list."""
    return len(list(filter(lambda x: x % 2 == 1, lst)))


def f2(lst):
    """Print each odd element in the given list."""
    print(*filter(lambda x: x % 2 == 1, lst))


def f3(lst):
    """Return the sum of all odd elements in a list."""
    return sum(filter(lambda x: x % 2 == 1, lst))


def f4(lst):
    """Return the sum of all the index positions whose corresponding element is odd."""
    return sum(map(lambda x: x[0], filter(lambda x: x[1] % 2 == 1, enumerate(lst))))


def f5(lst):
    """Return the same list where each element has been squared."""
    return list(map(lambda x: x ** 2, lst))


def f6(lst):
    """Return the largest number in the given list."""
    return max(lst)


def f7(lst):
    """Return the average of all the numbers in a list."""
    return sum(lst) / len(lst)


def f8(a, b, n):
    """Print all the numbers divisible by n within the range a and b inclusive."""
    print(*[i for i in range(a, b + 1) if i % n == 0])


def f9(width, height):
    """Print an ASCII rectangle with the given width and height."""
    print(*list(map(lambda x: x * width, ['*' for h in range(height)])), sep='\n')


def f10(n):
    """Print a triangle with the given height n."""
    print(*['*' * (i + 1) for i in range(n)], sep='\n')


def f11(lst):
    """Return True if a list is sorted in descending order and False otherwise. Return True for an empty list."""
    if sorted(lst, reverse=True) == lst:
        return True
    else:
        return False


def f12(lst):
    """Return True if the list consists of all negative numbers and False otherwise. Return True for empty list."""
    return not any(filter(lambda x: x > 0, lst))


def f13(lst, target):
    """Return the index of the last occurrence of the target in the list."""
    return list(map(lambda x: x[0], filter(lambda x: x[1] == target, enumerate(lst))))[-1]


def f14(lst):
    """Return the index of the last negative number in a list."""
    return list(map(lambda x: x[0], filter(lambda x: x[1] < 0, enumerate(lst))))[-1]


def f15(lst):
    """Return the sum of all the elements at even index positions."""
    return sum(map(lambda x: x[1], filter(lambda x: x[0] % 2 == 0, enumerate(lst))))


def f16(n):
    """Print out an upside down triangle."""
    print(*['*' * i for i in reversed(range(n))], sep="\n")


def f17(lst):
    """Print every other element in a list in reverse order."""
    print(*lst[::-2])


def f18(n):
    """Return n!"""
    from math import factorial
    return factorial(n)


def f19(matrix):
    """Print the sum of each row of the matrix"""
    for row in matrix:
        print(sum(row))


def f20(matrix):
    """Print the diagonals of a square matrix."""
    print(*[matrix[i][i] for i in range(len(matrix))])


def f21(lst):
    """Print the factorial of each element of a list."""
    import math
    print(*list(map(lambda x: math.factorial(x), lst)))


def f22(lst):
    """Print a countdown starting from each element to zero for a given list."""
    for i in lst:
        print(*list(range(i, -1, -1)))


def f23(list1, list2):
    """Return a new list where each index in the new list corresponds to list1[index] + list2[index]."""
    return list(map(lambda x, y: x + y, list1, list2))


def f24(n):
    """Print all the numbers from 1 to n inclusive that are multiples of 2 or 3."""
    print(*list(filter(lambda x: x % 2 == 0 or x % 3 == 0, list(range(1, n + 1)))))


def f25(lst):
    """Return the largest value in a list."""
    if isinstance(lst[0], list):
        return f25(lst(map(lambda x: max(x), lst)))
    else:
        return max(lst)


def f26(lst):
    """Return the second largest value in a list."""
    return sorted(lst)[-2]


def f27(n):
    """Return the leftmost digit in n."""
    return int(str(n)[0])


def f28(lst):
    """Print the largest value of each of the nested lists in a given list."""
    print(max([j for i in lst for j in i]))
