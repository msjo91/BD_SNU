def make_dict_number(lst):
    """Return a dictionary structure consisting of 'element: frequency'."""
    counts = dict()
    for i in lst:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts


def make_dict_number_get(lst):
    counts = dict()
    for i in lst:
        counts[i] = counts.get(i, 0) + 1
    return counts


def most_frequent(lst):
    """Returns the element having the maximum value among frequencies."""
    max_val = None
    max_count = 0
    counts = dict()
    for i in lst:
        if i in counts:
            count = counts[i]
        else:
            count = 0
        count += 1

        counts[i] = count

        if count > max_count:
            max_count = count
            max_val = i

    return max_val


def most_frequent_get(lst):
    max_val = None
    max_count = 0
    counts = dict()
    for i in lst:
        count = counts.get(i, 0) + 1
        counts[i] = count

        if count > max_count:
            max_count = count
            max_val = i
    return max_val
