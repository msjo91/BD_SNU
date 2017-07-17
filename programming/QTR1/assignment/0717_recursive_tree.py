"""
A tree has a structure [value, left subtree, right subtree].
A binary search tree's left child is smaller than parent and right child is larger than parent.
"""


def f21(tree):
    """Return the height of a tree."""
    if tree == []:
        return 0
    else:
        return 1 + max(f21(tree[1]), f21(tree[2]))


def f22(tree):
    """Return the number of nodes in a tree."""
    if tree == []:
        return 0
    else:
        return 1 + f22(tree[1]) + f22(tree[2])


def f23(tree):
    """Return the sum of the nodes in a tree"""
    if tree == []:
        return 0
    else:
        return tree[0] + f23(tree[1]) + f23(tree[2])


def f24(tree):
    """Print out the values of a binary search tree in ascending order."""
    if tree == []:
        pass
    else:
        f24(tree[1])
        print(tree[0])
        f24(tree[2])


def f25(tree):
    """
    Return the smallest element in a binary search tree.
    Return -1 if the tree is empty.
    """
    if tree == []:
        return -1
    elif tree[1] == [] and tree[2] == []:
        return tree[0]
    else:
        return f25(tree[1])
