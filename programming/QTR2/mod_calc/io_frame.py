from statistics import *
from math import *
from random import *

from tkinter import Text, END
from tkinter.ttk import Frame, Label, Button


class IOFrame(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.inputlabel = Label(self, text=" Input  ")
        self.inputlabel.grid(row=0, column=0)
        self.inputentry = Text(self, height=3, width=50)
        self.inputentry.grid(row=0, column=1)
        self.runbtn = Button(self, text="Run", command=self.calculate)
        self.runbtn.grid(row=1, column=1)
        self.outputlabel = Label(self, text=" Output ")
        self.outputlabel.grid(row=2, column=0, pady=5)
        self.outputentry = Text(self, height=3, width=50)
        self.outputentry.grid(row=2, column=1, pady=5)

    def calculate(self):
        input_val = self.inputentry.get("1.0", END)
        try:
            new_input = eval(input_val)
            self.outputentry.delete('1.0', END)
            self.outputentry.insert(END, new_input)
        except (ValueError, TypeError, SyntaxError, ZeroDivisionError) as e:
            print(e)


class HelpFrame(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.label = Label(self, text="   Help   ")
        self.label.grid(row=0, column=0)
        self.entry = Text(self, height=5, width=50)
        self.entry.grid(row=0, column=1)
