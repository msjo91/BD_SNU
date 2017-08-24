from tkinter import Tk, Canvas, N, W, E, S

lastx, lasty = 0, 0


def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y


def add_line(event):
    global lastx, lasty
    canvas.create_line(lastx, lasty, event.x, event.y)


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", add_line)

root.mainloop()
