from tkinter import Label, RIDGE, Entry, SUNKEN, mainloop, Tk, Button

colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']


def pack_wid():
    """pack() method organizes widgets in blocks before placing them in the parent widget."""
    for c in colours:
        Label(text=c, relief=RIDGE, width=15).pack()
        Entry(bg=c, relief=SUNKEN, width=10).pack()
    return mainloop()


def grid_wid():
    """grid() method organizes widgets in a table-like structure in the parent widget."""
    r = 0
    for c in colours:
        Label(text=c, relief=RIDGE, width=15).grid(row=r, column=0)
        Entry(bg=c, relief=SUNKEN, width=10).grid(row=r, column=1)
        r += 1
    return mainloop()


def place_wid():
    """place() method organizes widgets by placing them in a specific position in the parent widget."""
    root = Tk()
    b = Button(root, text="Hello")
    b.pack()
    b.place(height=100, width=100)
    return root.mainloop()


pack_wid()
grid_wid()
place_wid()
