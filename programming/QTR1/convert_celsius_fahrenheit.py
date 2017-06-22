# A program to convert Celsius temperature to Fahrenheit.


def main():
    celsius = int(input("What is the Celsius temperature? "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is {} degrees fahrenheit.\n".format(fahrenheit))
    if fahrenheit >= 90:
        print("!!!Heat Warning!!!\nIt's really hot out there, be careful!")
    elif fahrenheit <= 30:
        print("!!!Cold Warning!!!\nBrrrrr. Be sure to dress warmly.")
    else:
        print("At least the temperature is nice.")
