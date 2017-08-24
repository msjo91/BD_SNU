from tkinter import Tk, StringVar, Label, RAISED

root = Tk()

var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)

var.set("Waddap!")
label.pack()

root.mainloop()
