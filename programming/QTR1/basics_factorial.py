# Program to compute the factorial of a number
# Illustrate "for loop" with an accumulator


def main():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    print("The factorial of {n} is {fact}".format(n=n, fact=fact))
