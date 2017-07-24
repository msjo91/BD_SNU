def double_each(some_list):
    """
    Take a list and return a new list that has each element in the input list repeated twice.
    """
    if len(some_list) == 0:
        return []
    else:
        return [some_list[0]] * 2 + double_each(some_list[1:])
