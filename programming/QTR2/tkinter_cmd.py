from time import strftime, localtime
from tkinter import Tk, Button


# This is not an event handler
def clicked():
    time = strftime("Day: %d %b %Y\nTime: %H : %M : %S %p", localtime())
    print(time)


root = Tk()

btn = Button(root, text="Give me time!", command=clicked)
btn.pack()

root.mainloop()
