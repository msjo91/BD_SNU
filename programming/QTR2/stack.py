class Stack:
    """Stack class using list"""

    def __init__(self):
        self.items = []

    def __iter__(self):
        return self.items.__iter__()

    def __str__(self):
        return self.items.__str__()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if self.items is False:
            return True
        else:
            return False

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


mystack = Stack()
