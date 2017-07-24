def select(lst, M):
    if len(lst) == 1:
        return lst
    elif len(lst) < M:
        for idx, val in enumerate(lst):
            return [lst.pop(M - len(lst) - 1)] + select(lst[idx:] + lst[:idx], M)
    else:
        for idx, val in enumerate(lst):
            if (idx + 1) % M == 0:
                return [val] + select(lst[idx + 1:] + lst[:idx], M)


def josephus(N, M):
    lst = [i for i in range(1, N + 1)]
    return select(lst, M)
