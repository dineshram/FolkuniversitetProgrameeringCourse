# -*- coding: utf-8 -*-
# @description: Eksempel på bruk av tråd. 
#				Her ønskes å vise hva som skjer dersom hovedtråden stopper før undertråder.
#				Legg spesielt merke til linje #24
#
#				Eksempel 1:   Tråden kjører med daemon = False,  
#						      Bakgrunnstråden fortsetter å kjøre etter at hovedprogrammet er ferdig.
#
#				Eksempel 2:	  daemon = True,  bakgrunnstråder stopper når programmet stopper.								

import threading
import time

def task():
	" Funksjon som vil bli kjørt i egen tråd"
	for n in xrange(10):
		time.sleep(1)
		print("hei")


# Lager tråd og knytter den mot en funksjon
# Funksjonen blir IKKE kjørt enda.
t = threading.Thread(target=task)
#t.daemon = True
t.start() # Nu kjør vi. Tråden kjører funksjonen i bakgrunnen.

# Hovdetråden går videre, og sover i 4 sekunder før den...
time.sleep(4)

# ... avslutter
print ("exiting the Main Program")