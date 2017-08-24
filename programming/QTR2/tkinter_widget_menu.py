from tkinter import Tk, Menu, Toplevel, Button


def donothing():
    filewin = Toplevel(root)
    btn = Button(filewin, text="Do-nothing button")
    btn.pack()


root = Tk()
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
