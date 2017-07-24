def is_reverse(string1, string2):
    """
    Take two strings and return True if string1 is the same as string2 except in reverse order.
    Return False otherwise.
    """
    if len(string1) != len(string2):
        return False
    elif len(string1) == 0 and len(string2) == 0:
        return True
    elif string1[0] == string2[-1]:
        return is_reverse(string1[1:], string2[:-1])
    else:
        return False
