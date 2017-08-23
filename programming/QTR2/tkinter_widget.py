from tkinter import Tk, Label, Button

root = Tk()

mylabel = Label(root, text="Hello! Label Widget")
mylabel.pack()

mybutton = Button(root, text="Press me! Button Widget")
mybutton.pack()

root.mainloop()
