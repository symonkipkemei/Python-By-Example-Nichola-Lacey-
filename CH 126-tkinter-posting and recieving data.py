"""
126
Create a program that will ask
the user to enter a number in a
box. When they click on a
button it will add that number
to a total and display it in
another box. This can be
repeated as many times as
they want and keep adding to
the total. There should be
another button that resets the
total back to 0 and empties the
original text box, ready for
them to start again.
"""

"""GRAPHICS USER INTERFACE"""

from tkinter import *


# commands
def add():
    userNum = textBox1.get()
    userNum = int(userNum)
    answer = (textBox2["text"])
    num = int(answer)
    total = num + userNum
    textBox2["text"] = total


def reset():
    total = 0
    textBox1.delete(0, END)
    textBox2["text"] = total


# create an instance of tkinter
win = Tk()

# Create a window
win.geometry("950x500")
win.title("Total game")
win["bg"] = "black"

# FIRST ROW
# Enter No label
label = Label(text="Enter No")
label.place(x=50, y=50, width=200, height=50)

# Text box 1 (Data Entry)
textBox1 = Entry(text=0)
textBox1.place(x=250, y=50, width=300, height=50)
textBox1["justify"] = "center"

# Add button
btn = Button(text="Add", command=add)
btn.place(x=600, y=50, width=300, height=50)

# SECOND ROW
# text box 2 (Message display)
textBox2 = Message(text=0)
textBox2.place(x=50, y=150, width=850, height=50)

# THIRD ROW
# Reset button
reset = Button(text="Reset Total", command=reset)
reset.place(x=50, y=250, width=850, height=50)

# run
win.mainloop()

# if you are dealing with integers
# then remember to set the message text to 0
# otherwise you will receive a warning indicating an invalid literal
