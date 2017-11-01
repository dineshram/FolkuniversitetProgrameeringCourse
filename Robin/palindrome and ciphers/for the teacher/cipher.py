# coding: utf-8
import string

print [ord(c) for c in string.uppercase]


def cipher(text, secret=13):
    """ quick implementation for my own python-golf amusement. (Robin)"""
    return "".join([chr(65+((ord(c)-65)+secret)%26) if c != " " else " " for c in text])


def cipher2(text, secret=13):
    """ bit less condenced version """
    deciphered = ""
    for c in text:
        if c == " ":
            deciphered += " "
        else:
            forskyvning = (ord(c) - 65 + secret) % 26
            deciphered += chr(65+forskyvning)
    return deciphered


def cipher_pedagogically(text, secret=13):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    A = alphabet[0] # Første bokstav
    Z = alphabet[-1] # Siste bokstav
    tegn = len(alphabet) #26 tegn
    melding = "" # Her vil den dekrypterte meldingen komme

    # For hvert tegn i text
    for c in text:
        # Henter ascii tallet for denne karrakteren
        # ord tar inn et tegn, og returnerer tallverdien for det tegnet.
        # Eksempelvis blir A -> 65, B -> 66 osv.
        num = ord(c)
        # Forskyver <secret> posisjoner:
        num = num + secret

        # Sjekker at vi ikke har kommet lenger enn
        # siste bokstav i alfabetet
        siste_bokstav = ord(Z)
        if num > siste_bokstav:
            delta = num - ord(Z)
            num = ord(A) + delta -1
        # Legger til den dekrypterte bokstaven
        melding += chr(num)
    return melding


if __name__ == '__main__':
    print cipher2("Revered now I live on O did I do no evil I wonder ever".upper())
    print cipher2(cipher2("Revered now I live on O did I do no evil I wonder ever".upper()))
    print cipher_pedagogically("Revered now I live on O did I do no evil I wonder ever".upper())
