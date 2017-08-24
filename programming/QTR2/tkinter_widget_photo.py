from tkinter import Tk, PhotoImage, Label

root = Tk()

photo = PhotoImage(file="wiggle.gif")

label = Label(root, image=photo, width=350, height=700)

label.pack()

root.mainloop()
