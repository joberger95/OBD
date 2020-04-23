from tkinter import *
import webbrowser


def open_yt_channel():
    webbrowser.open_new("https://www.youtube.com/?gl=FR")


# first window
window = Tk()

# cutom window
window.title("My App")

# screen size
window.geometry()
window.minsize(1080, 720)

# icon insert
# window.iconbitmap("logo.ico")

# color window
window.config(background="#a5a2a2")

# add frame
frame = Frame(window, bg="#a5a2a2")

# labels
label_title = Label(
    frame, text="Welcome on my app", font=("Arial", 40), bg="#a5a2a2", fg="black"
)
label_title.pack(expand=YES)

label_subtitle = Label(
    frame, text="Hello all", font=("Arial", 28), bg="#a5a2a2", fg="black"
)
label_subtitle.pack(expand=YES)

# add button
button = Button(
    frame,
    text="Go!",
    font=("Arial", 28),
    bg="black",
    fg="#a5a2a2",
    command=open_yt_channel,
)
button.pack(pady=25, fill=X)

# adding frame
frame.pack(expand=YES)

# display
window.mainloop()
