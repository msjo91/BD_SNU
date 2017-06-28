def max_item_length(table):
    max_len = 0
    rows = len(table)
    cols = len(table[0])
    for row in range(rows):
        for col in range(cols):
            max_len = max(max_len, len(str(table[row][col])))
    return max_len


def print_2d_list(table):
    if table is False:
        print([])
    rows = len(table)
    cols = len(table[0])
    field_width = max_item_length(table)
    print("[", end=" ")
    for row in range(rows):
        if row > 0:
            print("\n  ", end="")
        print("[", end="")
        for col in range(cols):
            if col > 0:
                print(",", end=" ")
            format_spec = "%{}s".format(str(field_width))
            print(format_spec % str(table[row][col]), end="")
        print("]", end="")
    print(" ]")
