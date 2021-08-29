"""
128
1 kilometre = 0.6214 miles and 1
mile = 1.6093 kilometres. Using
these figures, make a program
that will allow the user to
convert between miles and
kilometres.
"""

from tkinter import *

# INTERFACE

win = Tk()


# COMMANDS
def converter1():
    userNumKm = textBox1.get()
    userNumKm = int(userNumKm)
    answerMiles = userNumKm * 0.6214
    textBox2["text"] = answerMiles

def converter2():
    userNumMiles = textBox21.get()
    userNumMiles = int(userNumMiles)
    answerKm = userNumMiles * 1.6093
    textBox22["text"] = answerKm

# creating the Window interface

win.geometry("500x500")
win.title("converter")

# creating the window label

label1 = Label(text="DISTANCE CONVERTER")
label1.place(x=50, y=50, width=400, height=50)
label1["bg"] = "red"

# FIRST ROW
# Label 2
label2 = Label(text="KM TO MILES")
label2.place(x=50, y=150, width=100, height=50)
label2["bg"] = "red"

# TextBox1 ( entry box)
textBox1 = Entry(text=0)
textBox1.place(x=150, y=150, width=50, height=50)
textBox1["bg"] = "white"

# Label 3
label3 = Label(text="KM")
label3.place(x=200, y=150, width=50, height=50)
label3["bg"] = "red"

# TextBox2 ( message box)
textBox2 = Message(text=0)
textBox2.place(x=250, y=150, width=50, height=50)
textBox2["bg"] = "white"

# Label 4
label4 = Label(text="MILES")
label4.place(x=300, y=150, width=50, height=50)
label4["bg"] = "red"

# button 1(convert)
button1 = Button(text="CONVERT", command=converter1)
button1.place(x=350, y=150, width=100, height=50)
button1["bg"] = "yellow"

# SECOND ROW

# Label 2
label22 = Label(text="MILES TO KM")
label22.place(x=50, y=250, width=100, height=50)
label22["bg"] = "red"

# TextBox1 ( entry box)
textBox21 = Entry(text=1)
textBox21.place(x=150, y=250, width=50, height=50)
textBox21["bg"] = "white"

# Label 3
label23 = Label(text="MILES")
label23.place(x=200, y=250, width=50, height=50)
label23["bg"] = "red"

# TextBox2 ( message box)
textBox22 = Message(text=0)
textBox22.place(x=250, y=250, width=50, height=50)
textBox22["bg"] = "white"

# Label 4
label24 = Label(text="KM")
label24.place(x=300, y=250, width=50, height=50)
label24["bg"] = "red"

# button 1(convert)
button21 = Button(text="CONVERT", command=converter2)
button21.place(x=350, y=250, width=100, height=50)
button21["bg"] = "yellow"

# running the program
win.mainloop()
