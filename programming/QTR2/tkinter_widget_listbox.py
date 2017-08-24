from tkinter import Tk, Listbox

root = Tk()

lb = Listbox(root)

lb.insert(1, "Python")
lb.insert(2, "Perl")
lb.insert(3, "C")
lb.insert(4, "PHP")
lb.insert(5, "JSP")
lb.insert(6, "Ruby")

lb.pack()

root.mainloop()
