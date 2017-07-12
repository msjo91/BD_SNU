"""
Implementation of quick sort
Step 1 : Select a pivot (usually the first element).
Step 2 : Divide the unsorted list into two, one containing elements less than the pivot the other containing larger.
Step 3 : Repeat step 2 in each new lists.
Step 4 : Merge.
"""


def quick_sort(items):
    if len(items) > 1:
        pivot_idx = len(items) // 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_idx:
                if val < items[pivot_idx]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_idx]] + larger_items
