__author__ = 'dram'

import turtle

myTurtle = turtle.Turtle()
length = 1

for count in range (0, 15):
    myTurtle.forward(length),
    myTurtle.penup(),
    myTurtle.forward(length)
    myTurtle.pendown()
    count += 1
    length += 1

turtle.done()
