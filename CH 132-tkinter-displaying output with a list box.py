"""
132
Using the .csv file you created for the last
challenge, create a program that will allow
people to add names and ages to the list
and create a button that will display the
contents of the .csv file by importing it to a
list box.
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


def display():
    listBox1.delete(0, END)
    import csv
    # Get user file name
    filename = str(textBox1.get())
    filename = filename + ".csv"

    # open file
    file = open(filename, "r")
    faili = list(csv.reader(file))
    for x in faili:
        listBox1.insert(END, x)
    file.close()


# creating a window
win.title("writing to a csv file")
win.geometry("1000x700")

# COLUMN 1
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

# COLUMN 2

# Display to csv file (button)
button3 = Button(text="Display csv file", command=display)
button3.place(x=550, y=50, width=400, height=25)

# Listbox (List)
listBox1 = Listbox()
listBox1.place(x=550, y=150, width=400, height=350)

# RUN PROGRAM
win.mainloop()
