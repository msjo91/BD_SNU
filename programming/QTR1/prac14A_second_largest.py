def second_largest(lst):
    if lst[0] < lst[1]:
        fst = lst[1]
        snd = lst[0]
    else:
        fst = lst[0]
        snd = lst[1]

    for i in range(2, len(lst)):
        if snd >= lst[i]:
            continue
        elif lst >= lst[i] > snd:
            snd = lst[i]
        else:
            snd = fst
            fst = lst[i]
    return snd
