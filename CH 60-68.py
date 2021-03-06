
import turtle

"""
060
Draw a square.
"""


scr = turtle.Screen()
scr.bgcolor("yellow")


for x in range(0, 5):
    turtle.forward(100)
    turtle.left(90)

'''
061
Draw a triangle.
'''

for y in range(0, 3):
    turtle.forward(100)
    turtle.right(120)

'''
062
Draw a circle.
'''
# draw small lines with small angle changes to form a circle
for x in range(0, 360):
    turtle.forward(1)
    turtle.right(1)

'''
063
Draw three squares
in a row with a gap
between each. Fill
them using three
different colours.
'''

# use for loop to iterate the three squares
import random
for x in range(0,3):
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.shape("turtle")
    turtle.begin_fill()
    color = random.choice(["red", "blue", "green", "yellow"])
    turtle.color("black", color)
    for y in range(0, 4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()


# turtle begin and end fill go hand in hand


'''
064
Draw a five-pointed
star.

'''

turtle.color("black", "red")
turtle.begin_fill()
turtle.color("black", "red")
for y in range(0, 5):
    turtle.left(144)
    turtle.forward(50)

    turtle.forward(50)
turtle.end_fill()


'''
066
Draw an octagon that uses a different colour (randomly
selected from a list of six possible colours) for each line.
'''
import random

colors = random.choice(["red", "green", "yellow", "blue", "green"])
turtle.begin_fill()
turtle.color("black", colors)
for d in range(0, 8):
    turtle.forward(50)
    turtle.right(45)
turtle.end_fill()


'''
067
Create the following pattern:

'''


for x in range(0, 16):
    turtle.right(30)
    colors = random.choice(["red", "green", "yellow", "blue", "green"])
    turtle.begin_fill()
    turtle.color("black", colors)
    for d in range(0, 8):
        turtle.forward(50)
        turtle.right(45)
    turtle.end_fill()


'''
068
Draw a pattern that will change each time the
program is run. Use the random function to pick
the number of lines, the length of each line and
the angle of each turn.

'''
numberOfLines = random.randint(0, 9)
lengthOfLines = random.randint(10, 30)
angle = random.randint(0, 180)
color = random.choice(["red", "blue", "orange", "green", "purple", "black"])

for x in range(0, numberOfLines):
    turtle.begin_fill()
    turtle.color(color)
    turtle.forward(lengthOfLines)
    turtle.right(angle)
    turtle.end_fill()


