from tkinter import Tk, Canvas


def draw(canvas, width, height):
    canvas.create_rectangle(0, 0, 150, 150, fill="yellow")


def run_draw(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("Bye!")


run_draw(400, 200)
