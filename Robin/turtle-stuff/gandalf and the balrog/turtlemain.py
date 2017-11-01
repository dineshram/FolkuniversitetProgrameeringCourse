# -*- coding: utf-8 -*-
import turtle
import turtlecollide # Importererer turtlecollide.py
import wasd # importerer wasd.py

# Setter størrelsen på turtle-vinduet til 500 x 500 piksler
turtle.screensize(500, 500)

turtlecollide.makeline(250)

# Holder på antall ganger vi præver å bevege oss over linjen
i = 0

def checkrightfaceplant():
    #sjekker om turtle passerer forbudt linje
    global i
    step = 100 # Hvor langt turtle vil bevege seg

    # Om vi IKKE kolliderer med linjen
    if not turtlecollide.is_colliding(turtle.xcor()+step, 250):
        print("You may pass!")
        wasd.moveright()
    else:
        # Vi kolliderte med linjen
        print("Thou shall not pass!")

    # For å være litt artig, teller vi
    # antall ganger vi forsøker å gå over linjen.
    # Spillet tar slutt om vi forsøker mer enn 50
    # Ganger.
    i += 1
    if i > 50:
        print("game over")
        exit(0)

# wasd.py har bundet pil opp, ned, høyre og venstre
# men nå overskriver vi keybinden for
# høyre piltast.
# Vi skal nå sjekke at vi ikke kolliderer før vi evnt. beveger oss.
turtle.onkey(checkrightfaceplant, "Right")
turtle.onkey(checkrightfaceplant, "d")


# Listen kjøres
turtle.listen()
turtle.mainloop()