from tkinter import Tk, Label, Entry


def create_tbox(parent):
    tbox = Entry(root)
    tbox.grid(row=1, column=2, padx=10)


root = Tk()

create_tbox(root)

w = Label(root, text="Name", height=7)
w.grid(row=1, column=1)
