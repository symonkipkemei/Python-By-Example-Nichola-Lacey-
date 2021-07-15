
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

