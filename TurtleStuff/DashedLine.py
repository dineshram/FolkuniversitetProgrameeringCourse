__author__ = 'dram'

#Draw a dashed line. You can move the turtle without the turtle drawing its movement by using the turtle.penup() function;
# to tell it to draw again, use turtle.pendown().

#http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

import turtle

myTurtle = turtle.Turtle()

for i in range (0, 6):
    myTurtle.forward(2),
    myTurtle.penup(),
    myTurtle.forward(3)
    myTurtle.pendown()
    i += 1

turtle.done()