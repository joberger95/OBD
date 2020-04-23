from tkinter import *
from random import randint, choice
import string

window = Tk()
window.title("Password generator")
window.geometry("1080x720")
window.config(bg="#a5a2a2")


def generate_passwd():
    passwd_min = 6
    passwd_max = 12
    all_char = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_char) for x in range(randint(passwd_min, passwd_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# princpal frame
frame = Frame(window, bg="#a5a2a2")

# add picture
width = 300
height = 300
picture = PhotoImage(file="image.png").zoom(35).subsample(32)

canvas = Canvas(
    frame, width=width, height=height, bg="#a5a2a2", bd=0, highlightthickness=0
)
canvas.create_image(width / 2, height / 2, image=picture)
canvas.grid(row=0, column=0, sticky=W)

# second box
right_frame = Frame(frame, bg="#a5a2a2")
# label
label_title = Label(
    right_frame, text="Password", font=("Helvetica", 20), bg="#a5a2a2", fg="white"
)
label_title.pack()

password_entry = Entry(right_frame, font=("Helvetica", 20), bg="#a5a2a2", fg="white")
password_entry.pack()

generate_button = Button(
    right_frame,
    text="Generate",
    font=("Helvetica", 20),
    bg="#a5a2a2",
    fg="white",
    command=generate_passwd,
)
generate_button.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=W)

# frame
frame.pack(expand=YES)

window.mainloop()
