"""
Towers of Hanoi.

Rules:
 Move all disks on one tower to another empty tower.
 A larger disk cannot stack on a smaller disk.
 The number of steps should be the least.

 A disk of a smaller number is the smaller disk.
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
        if self.items == []:
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
        self.t_dict = {1: self.tower1, 2: self.tower2, 3: self.tower3}
        self.n = 0  # Move count

        disk_list = []
        for i in range(1, self.num_disk + 1):
            disk_list.append(i)

        for i in reversed(disk_list):
            self.tower1.push(i)

    def check(self):
        """List the stacked disk of each tower."""
        if self.tower1.is_empty():
            print("\nTower 1: No disk")
        else:
            print("\nTower 1: {}".format(self.tower1.items))
        if self.tower2.is_empty():
            print("Tower 2: No disk")
        else:
            print("Tower 2: {}".format(self.tower2.items))
        if self.tower3.is_empty():
            print("Tower 3: No disk\n")
        else:
            print("Tower 3: {}\n".format(self.tower3.items))

    def move(self, from_t, to_t):
        """Move a disk to another disk."""
        if self.t_dict[to_t].is_empty():
            self.n += 1
            disk = self.t_dict[from_t].pop()
            self.t_dict[to_t].push(disk)
            print("\nDisk {d} is transferred from Tower {f} to Tower {t}.".format(
                d=disk,
                f=from_t,
                t=to_t
            ))
        else:
            if self.t_dict[from_t].peek() < self.t_dict[to_t].peek():
                self.n += 1
                disk = self.t_dict[from_t].pop()
                self.t_dict[to_t].push(disk)
                print("\nDisk {d} is transferred from Tower {f} to Tower {t}.\n".format(
                    d=disk,
                    f=from_t,
                    t=to_t
                ))
            else:
                print("\nDisk {d1} cannot be transferred because Disk {d2} of Tower{t} is smaller.\n".format(
                    d1=self.t_dict[from_t].peek(),
                    d2=self.t_dict[to_t].peek(),
                    t=to_t
                ))

    def count(self):
        """Total move counts"""
        print("\nYour total moves: {}".format(self.n))


def play():
    num_disk = int(input("How many disks?\n"))
    toh = TOH(num_disk)
    toh.check()
    while True:
        from_t = int(input("Move disk from Tower:\n"))
        to_t = int(input("\nMove disk to Tower:\n"))
        toh.move(from_t, to_t)
        toh.check()
        if len(toh.tower2.items) == toh.n or len(toh.tower3.items) == toh.n:
            toh.count()
            print("Congratulations!")
            break


play()
