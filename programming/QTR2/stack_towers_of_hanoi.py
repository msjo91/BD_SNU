"""
Towers of Hanoi.

Rules:
 Move all disks on one tower to another empty tower.
 A larger disk cannot stack on a smaller disk.
 The number of steps should be the least.

 A disk with a smaller number in its name is the smaller disk.
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
    """Tower of Hanoi"""

    def __init__(self, num_disk, num_tower):
        self.num_disk = num_disk
        self.num_tower = num_tower

        tower_dict = {}
        for i in range(1, self.num_disk + 1):
            tower_dict["Tower {}".format(i)] = Stack()

        disk_list = []
        for i in range(1, self.num_tower + 1):
            disk_list.append("Disk {}".format(i))

        for i in disk_list:
            tower_dict["Tower 1"].push(i)
