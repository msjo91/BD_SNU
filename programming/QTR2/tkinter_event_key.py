from tkinter import Tk, Canvas

root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.pack()

arrow = 0


def print_arrow(event):
    global arrow
    canvas.delete(arrow)
    if event.keysym == "Up":
        arrow = canvas.create_polygon(210, 200, 190, 200, 190, 180, 180, 180, 200, 160, 220, 180, 210, 180,
                                      fill="yellow", outline="black")
    elif event.keysym == "Down":
        arrow = canvas.create_polygon(210, 200, 190, 200, 190, 220, 180, 220, 200, 240, 220, 220, 210, 220, fill="pink",
                                      outline="black")
    elif event.keysym == "Left":
        arrow = canvas.create_polygon(200, 190, 200, 210, 180, 210, 180, 220, 160, 200, 180, 180, 180, 190,
                                      fill="lightblue", outline="black")
    elif event.keysym == "Right":
        arrow = canvas.create_polygon(200, 190, 200, 210, 220, 210, 220, 220, 240, 200, 220, 180, 220, 190,
                                      fill="white", outline="black")


canvas.bind_all('<KeyPress-Up>', print_arrow)
canvas.bind_all('<KeyPress-Down>', print_arrow)
canvas.bind_all('<KeyPress-Left>', print_arrow)
canvas.bind_all('<KeyPress-Right>', print_arrow)

root.mainloop()
