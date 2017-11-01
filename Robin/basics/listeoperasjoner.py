# coding: utf-8
#Øk alle elementene i listen med en.

liste = range(13)
print(liste)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in range(len(liste)):
	liste[i] = liste[i] + 1

print(liste)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# En annen måte, er å bruke et generator uttrykk
liste = [element + 1 for element in liste]
print(liste)
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def adder(tall, med=1):
	"returnerer summen av tallene <tall> og <med>"
	return tall + med


def substrakter(tall, med=2):
	"returnerer <tall> - <med>"
	return tall - med


# Map brukes for å utføre en funksjon på hvert
# element i en liste. map har argumentene: <funksjon> og <liste>
# Dereetter vil den internt gå igjennom alle elementene i
# listen <liste> og utføre funksjonen <funksjon> med <liste>
# som argument. 
liste = map(adder, liste)
print(liste)
# [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

liste = map(substrakter, liste)
print(liste)
