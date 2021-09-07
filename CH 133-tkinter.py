# lets proceed to tkinter advanced
from tkinter import *

win = Tk()

# changing the default icon
# refused to change icon
# win.wm_iconbitmap("icon.gif")


# creating the window
win.geometry("500x500")
win.title("trial")

# changing the background
win.configure(background="light green")

# Displaying an image in a label widget
logo = PhotoImage(file="logo.pbm")
logoImage = Label(image=logo)
logoImage.place(x=50, y=50)

# making the photo updatable
photo = PhotoImage(file="logo.pbm")
photoBox = Label(image=logo)
photoBox.image = photo
photoBox.place(x=50, y=250, width=200, height= 100)


# creating a drop down list
selectName = StringVar(win)
selectName.set("symon")
namesList = OptionMenu(win,selectName,"Sammy", "kipchumba", "soy")
namesList.place(x=50, y=350)

# clicked programme
sel = s


# running the programme
win.mainloop()
