from tkinter import Tk, Button

root = Tk()

b1 = Button(root, text="Ok", height=5, width=20)
b1.pack()
b2 = Button(root, text="Cancel", height=5, width=20)
b2.pack()

root.mainloop()
