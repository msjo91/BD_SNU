def f1(li):
    """Return the number of odd elements in a given list."""
    count = 0
    for i in li:
        if i % 2 == 1:
            count += 1
    return count


def f2(li):
    """Print each odd element in a given list."""
    for i in li:
        if i % 2 == 1:
            print(i)


def f3(li):
    """Return the sum of all odd elements in a given list."""
    res = 0
    for i in li:
        if i % 2 == 1:
            res += i
    return res


def f4(li):
    """Return the sum of all index positions whose corresponding element is odd in a given list."""
    res = 0
    for idx in range(len(li)):
        if li[idx] % 2 == 1:
            res += idx
    return res


def f5(li):
    """Return the same list where each element has been squared."""
    new_li = []
    for i in li:
        new_li.append(i ** 2)
    return new_li


def f6(li):
    """Return the largest number in a given list."""
    mx = li[0]
    for i in li:
        if i > mx:
            mx = i
    return mx


def f7(li):
    """Return the average of all the numbers in a given list."""
    total = 0
    num = len(li)
    for i in li:
        total += i
    return total / num


def f8(a, b, n):
    """Print all the numbers divisible by n within the range a and b inclusive."""
    for i in range(a, b):
        if i % n == 0:
            print(i)


def f9(width, height):
    """Print an ASCII rectangle with the given width and height."""
    if width == 0:
        pass
    else:
        for i in range(height):
            print('*' * width)


def f10(n):
    """Print a triangle with the given height n."""
    for i in range(n):
        print('*' * (i + 1))


def f11(li):
    """Return True if a list is sorted in descending order and False otherwise. Return True for an empty list."""
    if len(li) == 0 or len(li) == 1:
        return True
    for i in range(len(li) - 1):
        if li[i] < li[i + 1]:
            return False
        else:
            return True


def f12(li):
    """Return True if a list consists of all negative nubers and False otherwise. Return True for an empty list."""
    for idx in range(len(li)):
        if li[idx] > 0:
            return False
    return True


def f13(li, target):
    """Return the index of the last occurrence of target in a list."""
    if li.count(target) == 0:
        print("Misfire!")
    else:
        for i in range(len(li)):
            if target == li[i]:
                idx = i
        return idx


def f14(li):
    """Return the index of the last negative number in a list."""
    if all(i >= 0 for i in li):
        print("Give negative numbers!")
    else:
        for i in range(len(li)):
            if li[i] < 0:
                idx = i
        return idx


def f15(li):
    """Return the sum of all the elements at even index positions."""
    even_sum = 0
    for i in range(len(li)):
        if i % 2 == 0 and i != 0:
            even_sum += li[i]
    return even_sum


def f16(n):
    """Print out an upside down triangle."""
    for i in reversed(range(n)):
        print('*' * (i + 1))


def f17(li):
    """Print out every unique element in a list in reverse order."""
    for i in reversed(li):
        if li.count(i) == 1:
            print(i)


def f18(n):
    """Return n!."""
    if n < 0:
        print("Seriously? Go google 'gamma function'!")
    else:
        fact = 1
        for factor in range(n, 1, -1):
            fact *= factor
        return fact


def f19(li):
    """Print the factorial of each element of a given list."""
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
    """Print a countdown starting from each element to zero for a given list."""
    for i in li:
        for n in reversed(range(i + 1)):
            if n == 0:
                print(n)
            else:
                print(n, end=' ')


def f21(li1, li2):
    """Return a new list where each index in the new list corresponds to list1[index] + list2[index]."""
    if len(li1) != len(li2):
        print("Both lists should have the same length!")
    else:
        new_li = []
        for i in range(len(li1)):
            new_li.append(li1[i] + li2[i])
        return new_li


def f22(n):
    """Print all the numbers from 1 to n inclusive that is a multiple of 2 or 3."""
    for i in range(2, n + 1):
        if i % 2 == 0 or i % 3 == 0:
            print(i)


def f23(li):
    """Return the largest value in the list (of all the nested lists inside list)."""
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
        return mx


def f24(li):
    """Return the second largest value in the list."""
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
    """Return the leftmost digit in n."""
    try:
        return int(str(n)[0])
    except ValueError:
        print("Use a non-negative number!")


def f26(li):
    """Print the largest value of each of the nested lists in a given list."""
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
            print(mx)
