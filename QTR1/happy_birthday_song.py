def sing(name):
    v1 = "Happy birthday"
    v2 = " to you!\n"
    v3 = ", dear {}!\n".format(name)
    vr = v1 + v2
    print(vr * 2 + (v1 + v3) + vr)
