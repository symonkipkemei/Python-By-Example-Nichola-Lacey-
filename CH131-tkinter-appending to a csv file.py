"""
131
Create a program that will allow the
user to create a new .csv file. It should
ask them to enter the name and age of
a person and then allow them to add
this to the end of the file they have
just created.
"""

from tkinter import *

win = Tk()


# COMMANDS

def create():
    global fileName1
    try:
        userFileNameA = textBox1.get()
        fileName1 = str(userFileNameA) + ".csv"
        # creating a csv file
        file = open(fileName1, "x")
        file.close()
        msg2 = "okay"
        textWarning["text"] = msg2
        textWarning["bg"] = "blue"
        textWarning["fg"] = "white"
        textWarning["relief"] = "groove"

    except FileExistsError:
        msg1 = "file exists"
        textWarning["text"] = msg1
        textWarning["bg"] = "red"
        textWarning["fg"] = "white"
        textWarning["relief"] = "groove"
    return fileName1


def save():
    # Get user file name
    filename = str(textBox1.get())
    filename = filename + ".csv"
    # Get user details
    userName = str(textBox2.get())
    userAge = str(textBox3.get())

    # Save to user file name
    csvData = userName + "," + userAge + "\n"
    file = open(filename, "a")
    file.write(csvData)
    file.close()
    textBox2.delete(0, END)
    textBox3.delete(0, END)


# creating a window

win.title("writing to a csv file")
win.geometry("500x1000")

# WARNING MESSAGE
textWarning = Message(text="")
textWarning.place(x=50, y=50, width=400, height=25)

# enter name of csv label(label)
label1 = Label(text="Name of csv file")
label1.place(x=50, y=150, width=100, height=50)
label1["relief"] = "ridge"

# enter preferred name of csv file(Entry box)
textBox1 = Entry(text="")
textBox1.place(x=150, y=150, width=200, height=50)
textBox1["bg"] = "white"
textBox1["relief"] = "groove"

# create csv file button(button)
button1 = Button(text="Create", command=create)
button1.place(x=350, y=150, width=100, height=50)

# **** CONTENT******


# ROW 1
# enter your name (label)
label2 = Label(text="Your name")
label2.place(x=50, y=250, width=100, height=50)
label2["relief"] = "ridge"

# enter you name (entry box)
textBox2 = Entry(text="")
textBox2.place(x=150, y=250, width=300, height=50)
textBox2["bg"] = "white"
textBox2["relief"] = "groove"

# ROW2
# enter your age (label)
label2 = Label(text="Your Age")
label2.place(x=50, y=350, width=100, height=50)
label2["relief"] = "ridge"
# enter you age (entry box)
textBox3 = Entry(text=0)
textBox3.place(x=150, y=350, width=300, height=50)
textBox3["bg"] = "white"
textBox3["relief"] = "groove"

# ROW 3
# save to csv file (button)
button2 = Button(text="Save  to csv file", command=save)
button2.place(x=50, y=450, width=400, height=50)

# RUN PROGRAM
win.mainloop()
