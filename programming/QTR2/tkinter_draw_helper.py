from tkinter import Tk, Canvas


def draw_belgian(canvas, x0, y0, x1, y1):
    """
    Draw a Belgian flag in the area bounded by (x0, y0) in the top-left and (x1, y1) in the bottom-right.
    """
    width = x1 - x0
    canvas.create_rectangle(x0, y0, x0 + width / 3, y1, fill="black", width=0)
    canvas.create_rectangle(x0 + width / 3, y0, x0 + width * 2 / 3, y1, fill="yellow", width=0)
    canvas.create_rectangle(x0 + width * 2 / 3, y0, x1, y1, fill="red", width=0)


def draw(canvas, width, height):
    # Draw a large Belgian flag
    draw_belgian(canvas, 25, 25, 175, 150)
    # Draw a smaller one below it
    draw_belgian(canvas, 75, 160, 125, 200)

    # Draw a whole grid of Belgian flags
    flag_width = 30
    flag_height = 25
    margin = 5
    for row in range(4):
        for col in range(6):
            left = 200 + col * flag_width + margin
            top = 50 + row * flag_height + margin
            right = left + flag_width - margin
            bottom = top + flag_height - margin
            draw_belgian(canvas, left, top, right, bottom)


def run_draw(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("Bye!")


run_draw(400, 200)
