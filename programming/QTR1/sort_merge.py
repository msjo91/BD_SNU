def merge(l, r):
    idx_l = 0
    idx_r = 0
    new_li = []
    while idx_l < len(l) and idx_r < len(r):
        if l[idx_l] < r[idx_r]:
            new_li.append(l[idx_l])
            idx_l += 1
        else:
            new_li.append(r[idx_r])
            idx_r += 1
    # When the loop is broken, at least one loop is at its end.
    # Add the leftovers.
    new_li.extend(l[idx_l:])
    new_li.extend(r[idx_r:])
    return new_li


def msort(li):
    if len(li) <= 1:  # base case
        return li
    else:  # recursive case
        halfway = len(li) // 2
        li1 = li[0:halfway]
        li2 = li[halfway:]
        new_li1 = msort(li1)  # recursively sort left half
        new_li2 = msort(li2)  # recursively sort right half
        new_li = merge(new_li1, new_li2)
        return new_li
