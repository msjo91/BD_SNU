from tkinter import Tk, Canvas


def draw(canvas, width, height):
    pass  # Fill with custom drawing code


def run_draw(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("Bye!")


run_draw(400, 200)
