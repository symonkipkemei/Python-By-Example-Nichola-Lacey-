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


def call():
    name = textBox1.get()
    msg = str("hello " + name)
    textBox2["bg"] = "red"
    textBox2["fg"] = "white"
    textBox2["text"] = msg


# create an instance of tkinter
win = Tk()

# create a window
win.geometry("800x500")
win.title("hello user")

# create textbox1(Data ENTRY)

textBox1 = Entry(text="")
textBox1.place(x=50, y=50, width=100, height=30)
textBox1["justify"] = "center"
textBox1.focus()

# button
bt = Button(text="press me", command=call)
bt.place(x=160, y=50, width=100, height=30)

# create textbox2
textBox2 = Message(text="")
textBox2.place(x=160, y=100, width=100, height=30)

# run
win.mainloop()
