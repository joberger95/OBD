from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.title("ODB App")
        self.config(bg="#c3c0bf")
        self.geometry("%dx%d" % (width, height))

        self.frame = Frame(self, width=width / 10, height=height / 10, bg="white")
        self.frame.pack()

        self.splash_screen()
        self.asking_fields()

    def splash_screen(self):
        return None

    def asking_fields(self):
        self.string_field = StringVar()
        self.field1 = Entry(self.frame, textvariable=self.string_field)
        self.field1.grid(column=0, row=0)


window = Window()
window.mainloop()
