"""
Create a window that will
ask the user to enter their
name. When they click on
a button it should display
the message “Hello” and
their name and change
the background colour
and font colour of the
message box
"""

from tkinter import *

# create an instance of tkinter
win = Tk()

# create a window
win.geometry("800x500")
win.title("hello user")

# create a blank entry box
ent = Entry(text=0)
ent.place(x=50, y=50, width=100, height=30)


# create an action on pressing the button

def press():
    name = ent.get()
    msg = Message(text="hello " + name)
    msg.place(x=160, y=100, width=100, height=30)
    msg["bg"] = "white"
    msg["fg"] = "black"
    msg["relief"] = "sunken"


# button
bt = Button(text="press me", command=press)
bt.place(x=160, y=50, width=100, height=30)
# run
win.mainloop()
