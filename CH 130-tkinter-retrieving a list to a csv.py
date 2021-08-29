"""
129
Create a window that will ask the
user to enter a number in a text box.
When they click on a button it will
use the code
variable.isdigit() to check
to see if it is a whole number. If it is
a whole number, add it to a list box,
otherwise clear the entry box. Add
another button that will clear the
list.


"""

# What do we know
# GUI interface for window ,button,textbox and listbox

from tkinter import *

win = Tk()


def check():
    # we will check later on checking if a digit is a whole number
    # lets check if the user value is greater or less than 10
    variable = int(textBox1.get())
    if variable <= 40:
        listBox.insert(END, variable)
    else:
        textBox1.delete(0, END)


def clear():
    listBox.delete(0, END)


def csv():
    file = open("CH130-tkinter-list.csv", "a")
    listA = listBox.get(0, END)
    for x in listA:
        record = str(x) + "\n"
        file.write(record)


# creating a window
win.title("listing")
win.geometry("500x500")

# creating a label
label1 = Label(text="Enter a number")
label1.place(x=50, y=150, width=100, height=50)
label1["relief"] = "ridge"

# create a textbox
textBox1 = Entry(text=0)
textBox1.place(x=150, y=150, width=200, height=50)
textBox1["bg"] = "white"
textBox1["relief"] = "groove"

# create a button
button1 = Button(text="Check", command=check)
button1.place(x=350, y=150, width=100, height=50)

# create a listbox
listBox = Listbox()
listBox.place(x=50, y=250, width=300, height=50)
listBox["justify"] = "center"

# create a clear button
button2 = Button(text="Clear", command=clear)
button2.place(x=350, y=250, width=100, height=50)

# create a csv button
button2 = Button(text="save to csv", command=csv)
button2.place(x=350, y=350, width=100, height=50)

# run the program
win.mainloop()
