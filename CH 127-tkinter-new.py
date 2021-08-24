"""
127
Create a window that will ask the user to enter a
name in a text box. When they click on a button it
will add it to the end of the list that is displayed on
the screen. Create another button which will clear
the list.
"""

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
win.title("listing")
win["bg"] = "black"

# FIRST ROW
# Enter No label
label = Label(text="Enter your name")
label.place(x=50, y=50, width=200, height=50)

# Text box 1 (Data Entry)
textBox1 = Entry(text=0)
textBox1.place(x=250, y=50, width=300, height=50)
textBox1["justify"] = "center"

# Add button
button1 = Button(text="Add", command=add)
button1.place(x=600, y=50, width=150, height=50)

# Reset button
button2 = Button(text="Reset", command=add)
button2.place(x=750, y=50, width=150, height=50)

# run
win.mainloop()