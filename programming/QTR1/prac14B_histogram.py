def histogram_get(d):
    """
    Take a dictionary and return another dictionary representing a histogram of the original dictionary's values.
    """
    lst = list(d.values())
    counts = dict()
    for i in lst:
        counts[i] = counts.get(i, 0) + 1
    return counts


def histogram(d):
    ans = {}
    valuelist = list(d.values())
    for i in range(0, len(d)):
        ans[valuelist[i]] = valuelist.count(valuelist[i])
    return ans
