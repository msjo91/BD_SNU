def first_perfect_square(numbers):
    """
    Take a list of integers (which might be empty) as a parameter.
    It should return the index of the first number in the list that is a perfect square.
    If no element of the list is a perfect square, return -1.
    """
    for i in range(0, len(numbers)):
        if numbers[i] >= 0:
            if numbers[i] ** 0.5 - int(numbers[i] ** 0.5) == 0:
                return i
    return -1


def num_perfect_squares(numbers):
    """
    Take a list of integers (which might be empty) as a parameter.
    It should return the number of elements of the input list that are perfect squares.
    """
    count = 0
    for i in range(0, len(numbers)):
        if numbers[i] >= 0:
            continue
        if numbers[i] ** 0.5 - int(numbers[i] ** 0.5) == 0:
            count = count + 1
    return count
