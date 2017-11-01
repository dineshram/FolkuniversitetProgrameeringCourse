# coding: utf-8
import turtle
import math


def trekant(x=100.0, y=60.0):
    """ Tegner en rettvinklet trekant som har
        bunnlinje x=100, motliggende side y=60
        og den spisseste vinkelen er 30 grader.

        Det vil si, nå tegner den nesten hele trekanten,
        to steg mangler. Hva må til for å fullføre?

        Hint:   For å få en oversikt kan det være greit å
                kjøre funksjonen som den er og se hva som
                skjer.
        """
    # Pytagoras settning:
    # h = hypotenusen
    # x = langsiden
    # y = kortsiden
    #
    # h^2 = x^2 + y^2

    # dermed er h = kvadratroten av (x^2 + y^2)
    h = math.sqrt(x*x + y*y)
    # Vinklene i trekanten
    a,b,c = (30, 90, 120)

    # Tegner langsiden
    turtle.forward(x)
    # Snur 90 grader
    turtle.left(b)

    # Tegner kortsiden
    turtle.forward(y)

    # ---------------------------------------------------------------------
    # Til Dino:
    #    Her kan du viske ut disse to siste stegene, og la dem finne ut det selv. 
    # ----------------------------------------------------------------------
    
    # Siste sving
    turtle.left(c)

    # Og kjører i mål!
    turtle.forward(h)


# Kaller funksjonen
trekant()
# La stå!
turtle.exitonclick()
