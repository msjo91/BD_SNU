def sort_repeated(L):
    """Return a sorted list of the repeated elements in list L."""
    new_set = set()
    for i in L:
        if L.count(i) > 1:
            new_set.add(i)
    return sorted(new_set)
