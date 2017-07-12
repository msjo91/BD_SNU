"""
Implementation of insertion sort
Step 1 : Create an empty sorted list.
Step 2 : Move each element from the unsorted list one-by-one.
Step 3 : Keep the sorted list sorted.

Note : The unsorted list is preserved while having a new sorted list.
Note : The below code will just swap places.
"""


def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
