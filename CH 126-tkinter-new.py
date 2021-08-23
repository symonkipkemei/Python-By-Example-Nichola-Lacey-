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

# create an instance of tkinter
win = Tk()

# create a window
win.geometry("950x500")
win.title("Total game")
win["bg"] = "black"

# FIRST ROW
# enter No label
label = Label(text="Enter No")
label.place(x=50, y=50, width=200, height=50)

# entry box
ent = Entry(text=0)
ent.place(x=250, y=50, width=300, height=50)

num = ent.get()


# add button
btn = Button(text="Add")
btn.place(x=600, y=50, width=300, height=50)

# SECOND ROW
# Message box

msg = Message(text=num)
msg.place(x=50, y=150, width=850, height=50)

# THIRD ROW
# Reset button
reset = Button(text="Reset Total")
reset.place(x=50, y=250, width=850, height=50)

# run
win.mainloop()
