from tkinter import Tk, Canvas


def rgb_str(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)


def draw(canvas, width, height):
    pistachio = rgb_str(147, 197, 114)
    maroon = rgb_str(176, 48, 96)
    canvas.create_rectangle(0, 0, width / 2, height / 2, fill=pistachio)
    canvas.create_rectangle(width / 2, height / 2, width, height, fill=maroon)


def run_draw(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("Bye!")


run_draw(400, 200)
