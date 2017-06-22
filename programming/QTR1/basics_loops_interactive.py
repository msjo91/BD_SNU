def main():
    moredata = "yes"
    sum = 0.0
    count = 0
    while moredata[0] == 'y':
        x = int(input("Enter a number: "))
        sum += x
        count += 1
        moredata = input("More numbers (y or n)? ")
        print("\nThe average of the numbers is {}".format(sum / count))
