def low(tekst):
    alfabet1= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabet2="abcdefghijklmnopqrstuvwxyz"
    b = ""


    for x in range(len(tekst)):
        if tekst[x] in alfabet1:
            for n in range(len(alfabet1)):
                if tekst[x]== alfabet1[n]:
                    b += alfabet2[n]
        else:
            b += tekst[x]

    return(b)

print(low("FroKOsT"))