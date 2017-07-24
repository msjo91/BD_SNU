def count_matches(some_list, value):
    """
    Take a list and a value and count the number of elements in the list that are equal to the value.
    """
    if len(some_list) < 2:
        if len(some_list) == 0:
            return 0
        elif some_list[0] == value:
            return 1
        else:
            return 0
    return count_matches([some_list[0]], value) + count_matches(some_list[1:], value)
