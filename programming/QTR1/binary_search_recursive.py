# main function
def bsearch(items, key):
    return bs_helper(items, key, -1, len(items))


# recursive helper function
def bs_helper(items, key, lower, upper):
    if lower + 1 == upper:  # Base case : empty
        return None
    mid = (lower + upper) // 2  # Recursive case
    if key == items[mid]:
        return mid
    elif key < items[mid]:  # Go left
        return bs_helper(items, key, lower, mid)
    else:  # Go right
        return bs_helper(items, key, mid, upper)
