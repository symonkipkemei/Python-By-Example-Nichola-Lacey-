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

# create an instance of tkinter
win = Tk()

# create a window
win.geometry("400x200")
win.title("Dice")
win["bg"] = "black"


# create an action on pressing the button
def dice():
    num = random.randint(1, 6)
    msg = Message(text=num)
    msg.place(x=160, y=100, width=100, height=30)
    msg["bg"] = "white"
    msg["fg"] = "black"
    msg["relief"] = "sunken"


# button
bt = Button(text="dice me", command=dice)
bt.place(x=160, y=50, width=100, height=30)
# run
win.mainloop()
