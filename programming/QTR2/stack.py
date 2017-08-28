class Stack:
    """Stack class using list"""

    def __init__(self):
        self.items = []

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


mystack = Stack()
