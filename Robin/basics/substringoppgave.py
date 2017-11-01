#coding: utf-8

# Her er en måte å angi en streng som går over flere linjer.
# triple-quotes . Både """ og ''' kan brukes. Merk at man da kan
# bruke enkle anførselstegn inne i selve strengen :).
oppgave = """


	Gitt strengen 


		s="abcdefghijk"


	1 Hvordan kan du hente ut:
		a) første tegn? (a)
		b) siste tegn? (k)
		c) de første tre tegenene? (abc)
		d) alt bortsett fra det første tegnet? (bcdefghijk)
		e) alt bortsett fra det siste tegnet? (abcdefghij)
		f) de tre siste tegnene? (ijk)
		g) alt bortsett fra første og siste tegn? (bcdefghij)

	2 Kan du hente ut siste tegn på fler enn en måte? (k)
"""
# her er en faktisk python streng
# som brukes av svarene nedenfor
s="abcdefghijk"

# Splitter strengen opp i liste av linjene.
for linje in oppgave.split("\n"):
	print(linje)
	
	# Er dette et Spørsmål? da ber vi om svar :)
	if "?" in linje:
		# input tolker det man skriver som pythonkode,
		# og forsøker å kjøre det. 
		svar = input("\t\t\tDitt svar: ")
		print ("\t\t\tResultatet blir: %s\n" % svar)

		