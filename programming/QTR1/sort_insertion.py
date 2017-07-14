"""
Implementation of insertion sort
Step 1 : Create an empty sorted list.
Step 2 : Move each element from the unsorted list one-by-one.
Step 3 : Keep the sorted list sorted.

Note : The unsorted list is preserved while having a new sorted list.
Note : The below code will just swap places (It works this way as well).
"""


def insertion_sort(lst):
    s_counter = 0
    c_counter = 0
    for i in range(1, len(lst)):
        j = i
        if lst[j] >= lst[j - 1]:
            c_counter += 1
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
            s_counter += 1
            c_counter += 1
    return lst, "Total: {t} (Swaps: {s}, Compares: {c})".format(
        t=s_counter + c_counter,
        s=s_counter,
        c=c_counter
    )
