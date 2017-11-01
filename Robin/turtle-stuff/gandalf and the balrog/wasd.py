import turtle

def moveup():
    pos = turtle.position()
    turtle.goto(pos[0], pos[1] + 100)

def movedown():
    pos = turtle.position()
    turtle.goto(pos[0], pos[1] - 100)

def moveright():
    pos = turtle.position()
    turtle.goto(pos[0] + 100, pos[1])

def moveleft():
    pos = turtle.position()
    turtle.goto(pos[0] - 100, pos[1])

turtle.onkey(moveup, "Up")
turtle.onkey(moveup, "w")

turtle.onkey(movedown, "Down")
turtle.onkey(movedown, "s")

turtle.onkey(moveright, "Right")
turtle.onkey(moveright, "d")

turtle.onkey(moveleft, "Left")
turtle.onkey(moveleft, "a")

if __name__ == '__main__':
    turtle.onkey(turtle.reset, "space")

    turtle.listen()
    turtle.mainloop()