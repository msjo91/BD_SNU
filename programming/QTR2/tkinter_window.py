# Import tkinter (GUI package)
from tkinter import Tk, Label

# Create an instance from Tk class
root = Tk()  # Root window (a.k.a. base window, parent window) is where all widgets go

# Give title
root.title("A simple application")

# Create a label whose parent is "root"
w = Label(root, text="Hello, world!")  # Label is a widget that holds text

# Put the label into the window
w.pack()  # Without pack(), widgets are not displayed

# Run
root.mainloop()
