from operator import pos
import turtle

myFirstTurtle = turtle.Turtle()
mySecondTurtle = turtle.Turtle()

myFirstTurtle.color('yellow')
mySecondTurtle.color('red')
mySecondTurtle.speed(1000)

myFirstTurtle.begin_fill()
while True:
    myFirstTurtle.forward(200)
    myFirstTurtle.left(170)
    mySecondTurtle.forward(400)
    mySecondTurtle.left(170)
    #if abs(pos()) < 1:
     #   break

myFirstTurtle.end_fill()
turtle.done()
