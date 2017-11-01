import turtle

def makeline(x):
    turtle.up()
    turtle.goto(x, -500)
    turtle.pendown()
    turtle.goto(x, 500)
    turtle.up()
    turtle.goto(0, 0)
    turtle.pendown()

def is_colliding(turx, linex):
    if turx >= linex:
        n = True
    else:
        n = False
    return n

