# Sort list into ascending order
def sel_sort(li):
    n = len(li)

    # For each position in the list except the very last.
    for bottom in range(n - 1):

        # Find the smallest item in li[bottom] ... li[n - 1]
        mp = bottom  # bottom is smallest initially
        for i in range(bottom + 1, n):  # Look at each position
            if li[i] < li[mp]:  # This one is smaller
                mp = i  # Remember its index

        # Swap the smallest item to the bottom
        li[bottom], li[mp] = li[mp], li[bottom]
