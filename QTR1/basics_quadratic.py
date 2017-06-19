# A program that computes the real roots of a quadratic equation.
# Illustrates use of a multi-way decision.
import math


def main():
    print("This program finds the real solutions to a quadratic\n")
    a, b, c = eval(input("Plese enter the coefficients (a, b, c): "))

    discrim = b ** 2 - 4 * a * c
    if discrim < 0:
        print("\nThe equation has no real roots!")
    elif discrim == 0:
        root = -b / (2 * a)
        print("\nThere is a double root at {}".format(root))
    else:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are: {r1}, {r2}".format(r1=root1, r2=root2))
