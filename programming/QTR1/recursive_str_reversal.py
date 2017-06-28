def reverse(s, depth=0):
    print(" " * depth, "reverse({})".format(s))
    if s == "":
        result = s
    else:
        result = reverse(s[1:], depth + 1) + s[0]
    print(" " * depth, "-> {}".format(result))
    return result


def reverse2(s):
    if s == "":
        return s
    else:
        return s[-1] + reverse(s[:-1])
