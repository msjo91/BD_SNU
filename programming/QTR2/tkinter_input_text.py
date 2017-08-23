from tkinter import Tk, Text, END

root = Tk()

T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Just a text Widget\nin two line\n")

root.mainloop()
