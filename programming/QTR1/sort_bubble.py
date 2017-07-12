"""
Implementation of bubble sort
Step 1 : Compare first element and second element.
Step 2 : Swap if it meets the condition.
Step 3 : Repeat step 1 and 2 until (n - 1)-th element and n-th element (that is the last element) are examined.
"""


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap
