"""
Towers of Hanoi.

Rules:
 Move all disks on one tower to another empty tower.
 A larger disk cannot stack on a smaller disk.
 The number of steps should be the least.

 A disk with a smaller number in its name is the smaller disk.
 There are only three towers.
"""


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


class TOH:
    """Towers of Hanoi"""

    def __init__(self, num_disk):
        """Setup"""
        self.num_disk = num_disk
        self.tower1 = Stack()
        self.tower2 = Stack()
        self.tower3 = Stack()

        disk_list = []
        for i in range(1, self.num_disk + 1):
            disk_list.append(i)

        for i in reversed(disk_list):
            self.tower1.push(i)
