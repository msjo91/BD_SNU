from tkinter import Tk, IntVar, Checkbutton

root = Tk()

chkvar1 = IntVar()
chkvar2 = IntVar()

c1 = Checkbutton(root, text="Music", variable=chkvar1, onvalue=1, offvalue=0, height=5, width=20)
c1.pack()

c2 = Checkbutton(root, text="Video", variable=chkvar2, onvalue=1, offvalue=0, height=5, width=20)
c2.pack()

root.mainloop()
