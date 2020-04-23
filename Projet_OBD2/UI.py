from tkinter import *
import tkinter as tk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.title("ODB App")
        self.config(bg="#c3c0bf")
        self.geometry("%dx%d" % (width, height))

        self.splash_screen()

    def splash_screen(self):
        return None


window = Window()
window.mainloop()
