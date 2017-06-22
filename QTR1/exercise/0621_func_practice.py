def f1(li):
    num = 0
    for i in li:
        if i % 2 == 1:
            num += 1
    return num


def f2(li):
    for i in li:
        if i % 2 == 1:
            print(i)


def f3(li):
    num = 0
    for i in li:
        if i % 2 == 1:
            num += i
    return num


def f4(li):
    idx = 0
    for i in li:
        if i % 2 == 1:
            idx += li.index(i)
    return idx


def f5(li):
    sq = []
    for i in li:
        sq.append(i ** 2)
    return sq


def f6(li):
    mx = li[0]
    for i in li:
        if i > mx:
            mx = i
    return mx


def f7(li):
    sm = 0
    num = len(li)
    for i in li:
        sm += i
    return sm / num


def f8(a, b, n):
    for i in range(a, b):
        if i % n == 0:
            print(i)


def f9(width, height):
    if width == 0:
        for i in range(0):
            print('*' * width)
    else:
        for i in range(height):
            print('*' * width)


def f10(n):
    for i in range(n):
        print('*' * (i + 1))


def f11(li):
    if len(li) == 0 or len(li) == 1:
        return True
    for i in range(len(li) - 1):
        if li[i] < li[i + 1]:
            return False
        else:
            return True


def f12(li):
    if len(li) == 0:
        return True
    for i in li:
        if i < 0:
            return True
        else:
            return False


def f13(li, target):
    if li.count(target) == 0:
        print("Misfire!")
    else:
        for i in range(len(li)):
            if target == li[i]:
                idx = i
        return idx


def f14(li):
    if all(i >= 0 for i in li):
        print("No negative numbers!")
    else:
        for i in range(len(li)):
            if li[i] < 0:
                idx = i
        return idx


def f15(li):
    even_sum = 0
    for i in range(len(li)):
        if i % 2 == 0 and i != 0:
            even_sum += li[i]
    return even_sum


def f16(n):
    for i in reversed(range(n)):
        print('*' * (i + 1))


def f17(li):
    for i in reversed(li):
        if li.count(i) == 1:
            print(i)


def f18(n):
    if n < 0:
        print("Seriously? Go google 'gamma function'!")
    else:
        fact = 1
        for factor in range(n, 1, -1):
            fact *= factor
        return fact


def f19(li):
    if any(i < 0 for i in li):
        print("Again? Google 'factorial negative'!")
    else:
        fact = 1
        for i in li:
            for factor in range(i, 1, -1):
                fact *= factor
            print(fact)
            fact = 1


def f20(li):
    for i in li:
        for n in reversed(range(i + 1)):
            if n == 0:
                print(n)
            else:
                print(n, end=' ')


def f21(li1, li2):
    if len(li1) != len(li2):
        print("Both lists should have the same length!")
    else:
        new_li = []
        for i in range(len(li1)):
            new_li.append(li1[i] + li2[i])
        return new_li


def f22(n):
    for i in range(2, n + 1):
        if i % 2 == 0 or i % 3 == 0:
            print(i)


def f23(li):
    if any(type(sublist) != list for sublist in li):
        print("All elements are list type, period!")
    else:
        new_li = []
        for sublist in li:
            for i in sublist:
                new_li.append(i)
        mx = new_li[0]
        for i in new_li:
            if i > mx:
                mx = i
        print(mx)


def f24(li):
    if len(li) < 2:
        print("The list should have at least 2 elements!")
    else:
        mx = li[0]
        for i in li:
            if i > mx:
                mx = i
        li.pop(li.index(mx))
        mx = li[0]
        for i in li:
            if i > mx:
                mx = i
        return mx


def f25(n):
    try:
        return int(str(n)[0])
    except ValueError:
        print("Use a non-negative number!")


def f26(li):
    if any(type(sublist) != list for sublist in li):
        print("All elements should be list type!")
    elif any(sublist == [] for sublist in li):
        print("No empty list is allowed!")
    else:
        for sublist in li:
            mx = sublist[0]
            for i in sublist:
                if i > mx:
                    mx = i
            print(i)
