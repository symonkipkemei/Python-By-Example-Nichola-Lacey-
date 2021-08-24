"""
125
Write a program that
can be used instead
of rolling a six-sided
die in a board game.
When the user clicks
a button it should
display a random
whole number
between 1 to 6
(inclusive).
"""

from tkinter import *
import random


# create an action on pressing the button
def dice():
    num = random.randint(1, 6)
    textBox1["bg"] = "red"
    textBox1["fg"] = "white"
    textBox1["text"] = num


# create an instance of tkinter
win = Tk()

# create a window
win.geometry("400x200")
win.title("Dice")
win["bg"] = "black"


# button
bt = Button(text="dice me", command=dice)
bt.place(x=160, y=50, width=100, height=30)

# textbox1

textBox1 = Message(text="")
textBox1.place(x=160, y=100, width=100, height=30)
textBox1["bg"] = "white"
textBox1["fg"] = "black"
textBox1["relief"] = "sunken"

# run
win.mainloop()
