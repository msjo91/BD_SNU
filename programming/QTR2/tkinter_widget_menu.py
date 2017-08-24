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

# Draw a separator line.
filemenu.add_separator()

# Close.
filemenu.add_command(label="Exit", command=root.quit)

# Pack menu under label "File" (Drop-down style).
menubar.add_cascade(label="File", menu=filemenu)

# If root.config(menu=menubar) is not declared, system menu does not change.
root.config(menu=menubar)

# Run
root.mainloop()
