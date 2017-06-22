# Basic weights
# C -> carbon: 12.011, H -> hydrogen: 1.0079, O -> oxygen: 15.9994


def molecular_weight():
    print("Please enter the number of each atom")
    c = int(input("carbon: "))
    h = int(input("hydrogen: "))
    o = int(input("oxygen: "))
    w = c * 12.011 + h * 1.0079 + o * 15.9994
    print("The molecular weight of C {c}, H {h}, O {o} is: {w}".format(c=c, h=h, o=o, w=round(w, 2)))
