class HouseLannister:
    lastname = ' Lannister'

    def __init__(self, name):
        self.fullname = name + self.lastname

    def travel(self, where):
        print("{n} goes to {w}.".format(n=self.fullname, w=where))

    def love(self, other):
        print("{n1} and {n2} are in love.".format(n1=self.fullname, n2=other.fullname))

    def __add__(self, other):
        print("{n1} and {n2} are married.".format(n1=self.fullname, n2=other.fullname))

    def fight(self, other):
        print("{n1} and {n2} are in a fight.".format(n1=self.fullname, n2=other.fullname))

    def __sub__(self, other):
        print("{n1} and {n2} are divorced.".format(n1=self.fullname, n2=other.fullname))


class HouseStark(HouseLannister):
    lastname = ' Stark'

    def travel(self, where, day):
        print("{n} travels {w} for {d} days.".format(n=self.fullname, w=where, d=day))
