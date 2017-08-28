class Stack:
    """Stack class using list"""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        return self.items[len(self.items) - 1]


def parenthesis_matching(arg):
    mystack = Stack()
    for i in range(len(arg)):
        if arg[i] == "(":
            mystack.push(i)
        elif arg[i] == ")":
            if not mystack.is_empty():
                print((mystack.pop(), i))
