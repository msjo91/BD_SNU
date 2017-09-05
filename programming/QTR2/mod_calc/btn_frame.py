from tkinter import END
from tkinter.ttk import Frame, Label, Button

from instruction import instruction


class StatFrame(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.label = Label(self, text="Statistics")
        self.label.grid(row=0, column=0)
        self.func = ['mean', 'median', 'mode', 'pstdev', 'pvariance', 'stdev', 'variance']
        for idx, val in enumerate(self.func):
            self.btn = Button(self, text=val, width=8, command=lambda val=val: self.event(val))
            self.btn.grid(row=idx + 1, column=0)

    def event(self, val):
        self.master.helpframe.entry.delete('1.0', END)
        self.master.helpframe.entry.insert(END, instruction[val])


class MathFrame(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.label = Label(self, text="Math")
        self.label.grid(row=0, column=0, columnspan=2)
        func = ['ceil', 'floor', 'fabs', 'factorial', 'fmod', 'log', 'pow', 'sqrt',
                'sin', 'cos', 'tan', 'degrees', 'radians', 'cosh', 'sinh', 'tanh']
        for idx, val in enumerate(func):
            self.btn = Button(self, text=val, width=8)
            self.btn = Button(self, text=val, width=8, command=lambda val=val: self.event(val))
            if idx < 8:
                self.btn.grid(row=idx + 1, column=0)
            else:
                self.btn.grid(row=idx - 7, column=1)

    def event(self, val):
        self.master.helpframe.entry.delete('1.0', END)
        self.master.helpframe.entry.insert(END, instruction[val])


class RndFrame(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.label = Label(self, text="Random")
        self.label.grid(row=0, column=0)
        func = ['random', 'seed', 'uniform', 'randint', 'randrange', 'choice', 'shuffle', 'sample']
        for idx, val in enumerate(func):
            self.btn = Button(self, text=val, width=8)
            self.btn = Button(self, text=val, width=8, command=lambda val=val: self.event(val))
            self.btn.grid(row=idx + 1, column=0)

    def event(self, val):
        self.master.helpframe.entry.delete('1.0', END)
        self.master.helpframe.entry.insert(END, instruction[val])
