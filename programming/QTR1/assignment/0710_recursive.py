def f1(lst):
    """Return the sum of the elements in a list."""
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + f1(lst[1:])


def f2(n):
    """
    f(n) = { n // 2     if n is even;
             3 * n + 1  if n is odd; }
    Return the number of steps of the function f(n) until it reaches 1.
    Collatz Conjecture.
    """
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + f2(n // 2)
        else:
            return 1 + f2(3 * n + 1)


def f3(lst):
    """Print out the element in a list in reverse order."""
    if len(lst) == 0:
        pass
    else:
        print(lst[-1])
        return f3(lst[:-1])


def f4(lst):
    """Print out tripled odd elements."""
    if len(lst) == 0:
        pass
    else:
        if lst[0] % 2 == 1:
            print(lst[0] * 3)
            return f4(lst[1:])
        else:
            return f4(lst[1:])


def f5(lst):
    """Multiply odd elements by 3 and print all elements in reverse order."""
    if len(lst) == 0:
        pass
    else:
        if lst[-1] % 2 == 1:
            print(lst[-1] * 3)
            return f5(lst[:-1])
        else:
            print(lst[-1])
            return f5(lst[:-1])


def f6(lst):
    """Flatten a list."""
    if type(lst) != list or len(lst) == 0:
        return lst
    else:
        if type(lst[0]) != list:
            return [lst[0]] + f6(lst[1:])
        else:
            return f6(lst[0]) + f6(lst[1:])


def f7(n):
    """
    Ln = 2                if n = 0;
         1                if n = 1;
         Ln - 1 + Ln - 2  if n > 1;
    Calculate Ln.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return f7(n - 1) + f7(n - 2)


def f8(s):
    """Return True if s is palindrome and False otherwise."""
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return f8(s[1:-1])


def f9(n):
    """Return n!."""
    if n == 0:
        return 1
    else:
        return n * f9(n - 1)


def f10(lst):
    """Return len(lst)."""
    if len(lst) == 0:
        return 0
    else:
        return 1 + f10(lst[1:])


def f11(lst):
    """Return the last element in a list."""
    if len(lst) == 0:
        pass
    elif len(lst) == 1:
        return lst[0]
    else:
        return f11(lst[1:])


def f12(n):
    """Print the numbers n through 1 in descending order."""
    if n <= 0:
        pass
    else:
        print(n)
        return f12(n - 1)


def f13(n):
    """Return the number of digits in n."""
    if n // 10 == 0:
        return 1
    else:
        return 1 + f13(n // 10)


def f14(lst):
    """
    Return the first odd number or None if there are no odd numbers in a list.
    """
    if len(lst) == 0:
        return None
    else:
        if lst[0] % 2 == 1:
            return lst[0]
        else:
            return f14(lst[1:])


def f15(lst):
    """Return the sum of all odd numbers."""
    if len(lst) == 0:
        return 0
    else:
        if lst[0] % 2 == 1:
            return lst[0] + f15(lst[1:])
        else:
            return f15(lst[1:])


def f16(lst):
    """Return a list of odd numbers from the original list."""
    if len(lst) == 0:
        return []
    else:
        if lst[0] % 2 == 1:
            return [lst[0]] + f16(lst[1:])
        else:
            return f16(lst[1:])


def f17(lst):
    """Return the second to last element in a list."""
    if len(lst) == 2:
        return lst[0]
    else:
        return f17(lst[1:])


def f18(a, b):
    """Return the greatest common divisor of a and b."""
    if b == 0:
        return a
    else:
        return f18(b, a % b)


def f19(lst1, lst2):
    """Merge lst1 and lst2 in ascending order when each list is already sorted."""
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    else:
        if lst1[0] < lst2[0]:
            return [lst1[0]] + f19(lst1[1:], lst2)
        else:
            return [lst2[0]] + f19(lst1, lst2[1:])


def f20(lst):
    """Merge sort a list."""
    if len(lst) <= 1:
        return lst
    else:
        half = len(lst) // 2
        lst1 = lst[0:half]
        lst2 = lst[half:]
        new_lst1 = f20(lst1)
        new_lst2 = f20(lst2)
        new_lst = merge(new_lst1, new_lst2)
        return new_lst


def merge(l, r):
    idx_l = 0
    idx_r = 0
    new_lst = []
    while idx_l < len(l) and idx_r < len(r):
        if l[idx_l] < r[idx_r]:
            new_lst.append(l[idx_l])
            idx_l += 1
        else:
            new_lst.append(r[idx_r])
            idx_r += 1
    new_lst.extend(l[idx_l:])
    new_lst.extend(r[idx_r:])
    return new_lst
