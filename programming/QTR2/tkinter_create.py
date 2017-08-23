from tkinter import Tk, Canvas, N, W, E, S, PhotoImage

root = Tk()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create instance from Canvas class
canvas = Canvas(root)

canvas.grid(column=0, row=0, sticky=(N, W, E, S))

# Line
canvas.create_line((10, 10, 10, 100))
canvas.create_line((10, 10, 100, 10))

# Figure
canvas.create_rectangle(100, 100, 150, 150)
canvas.create_oval(200, 100, 250, 150)
canvas.create_arc(200, 200, 300, 300)
canvas.create_polygon(280, 150, 280, 100, 350, 150, 360, 100, 380, 250)

# Text
canvas.create_text(50, 200, text="canvas")

# Image
image = PhotoImage(file="wiggle.gif")
canvas.create_image(200, 40, image=image)

root.mainloop()
