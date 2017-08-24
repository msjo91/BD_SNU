from tkinter import Tk, Menu, Toplevel, Button


def donothing():
    filewin = Toplevel(root)
    btn = Button(filewin, text="Do-nothing button")
    btn.pack()


root = Tk()
menubar = Menu(root)

# Create file menu
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

# Draw a separator line.
filemenu.add_separator()

# Close.
filemenu.add_command(label="Exit", command=root.quit)

# Pack menu under label "File" (Drop-down style).
menubar.add_cascade(label="File", menu=filemenu)

# Create edit menu
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)

# Create help menu
helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About", command=donothing)

menubar.add_cascade(label="Help", menu=helpmenu)

# If root.config(menu=menubar) is not declared, system menu does not change.
root.config(menu=menubar)

# Run
root.mainloop()
