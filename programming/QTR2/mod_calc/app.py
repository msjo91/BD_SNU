from tkinter import N
from tkinter.ttk import Frame

from io_frame import IOFrame, HelpFrame
from btn_frame import StatFrame, MathFrame, RndFrame


class App(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.ioframe = IOFrame(self)
        self.ioframe.grid(row=0, column=0, columnspan=3)
        self.helpframe = HelpFrame(self)
        self.helpframe.grid(row=1, column=0, columnspan=3)
        self.statframe = StatFrame(self)
        self.statframe.grid(row=2, column=0, sticky=N)
        self.mathframe = MathFrame(self)
        self.mathframe.grid(row=2, column=1)
        self.rndframe = RndFrame(self)
        self.rndframe.grid(row=2, column=2)
