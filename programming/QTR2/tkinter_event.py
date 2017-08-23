from tkinter import Tk, Button
import sys

root = Tk()


# Event handlers
def hello(event):
    print("Single Click, Button-1")


def quit(event):
    print("Double Click, Double-Button-1")
    sys.exit()


wbutton = Button(root, text="Mouse Clicks")
wbutton.pack()

# Give hello() event handler '<Button-1>' event
wbutton.bind('<Button-1>', hello)
# Give quit() event handler '<Double-Button-1>' event
wbutton.bind('<Double-Button-1>', quit)

root.mainloop()
