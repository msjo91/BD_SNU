# Computes the average of numbers listed in a file.
# Works with multiple numbers on a line.
import string


def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            sum += eval(xStr)
            count += 1
        line = infile.readline()
    infile.close()
    print("\nThe average of the numbers is {}".format(sum / count))
