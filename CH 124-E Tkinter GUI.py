# imports all components of the tkinter library
from tkinter import *


def Call():
    msg = Label(window, text="you pressed the button")
    msg.place(x=30, y=50)
    button["bg"] = "blue"
    button["fg"] = "white"


# instance of tkinter
# which has been initialised by assigning it to a variable window
window = Tk()
# set the size  of the window
# tkinter uses the Cartesian plane to size and place components
# whereby x starts and moves horizontally followed by y which moves vertically
window.geometry("500x500")
window.title("tutorial")

# tkinter has several components
# they are
# Label-displays texts on screen
# Button-displays buttons
# Entry box- allows for input by the user
# Message- displays a message
# Listbox


# button object
button = Button(text="press me", command=Call)
button.place(x=30, y=20, width=120, height=25)

# label object
label = Label(text="Symon I am happy by how far you have come.Keep going.")
label.place(x=30, y=60)

# entry box object
entryBox = Entry(text="Live, love and laugh")
entryBox.place(x=30, y=100)

# output box object
outputBox = Message(text="Great so far")
outputBox["bg"]="red"
outputBox["fg"]="yellow"
outputBox["relief"]="sunken"

outputBox.place(x=30, y=130, width=100)

# ListBox object
cows =["zebu", "Ankole", "Fresian", "Gersian", "Teta"]
listBox = Listbox()


# what is the difference between a message and a label?

# run/compile
window.mainloop()
