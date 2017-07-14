"""
Implementation of quick sort
Step 1 : Select a pivot (usually the first element).
Step 2 : Divide the unsorted list into two, one containing elements less than the pivot the other containing larger.
Step 3 : Repeat step 2 in each new lists.
Step 4 : Merge.
"""

c_counter = 0
a_counter = 0
u_counter = 0


def quick_sort(items):
    global c_counter
    global a_counter
    global u_counter

    if len(items) > 1:
        pivot_idx = len(items) // 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):
            if i != pivot_idx:
                c_counter += 1
                if val < items[pivot_idx]:
                    smaller_items.append(val)
                    a_counter += 1
                else:
                    larger_items.append(val)
                    a_counter += 1
            else:
                c_counter += 1

        quick_sort(smaller_items)
        quick_sort(larger_items)
        items[:] = smaller_items + [items[pivot_idx]] + larger_items
        u_counter += 1
        return items, "Total: {t} (Compares: {c}, Appends: {a}, Unions: {u}".format(
            t=c_counter + a_counter + u_counter,
            c=c_counter,
            a=a_counter,
            u=u_counter
        )
