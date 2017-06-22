# A program to print the month name, given it's number.
# This version uses a list as a lookup table.


def main():
    # months is a list used as a lookup table
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    n = int(input("Enter a month in number (1-12): "))
    print("The month abbreviations is {}.".format(months[n - 1]))
