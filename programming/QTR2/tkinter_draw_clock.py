from math import pi, cos, sin
from tkinter import Tk, Canvas


def draw(canvas, width, height):
    (cx, cy, r) = (width / 2, height / 2, min(width, height) / 3)
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="yellow")
    r *= 0.85  # Make smaller so time labels lie inside clock face
    for hour in range(12):
        hour_angle = pi / 2 - (2 * pi) * (hour / 12)
        hour_x = cx + r * cos(hour_angle)
        hour_y = cy - r * sin(hour_angle)
        label = str(hour if hour > 0 else 12)
        canvas.create_text(hour_x, hour_y, text=label, font="Arial 16 bold")


def run_draw(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("Bye!")


run_draw(400, 200)
