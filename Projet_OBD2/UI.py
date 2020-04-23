from tkinter import *


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("ODB App")
        self.minsize(1080, 720)
        self.iconbitmap("motor.ico")


window = Window()
window.mainloop()
