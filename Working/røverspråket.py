
def røverspråket():
    a=input("Give a word : ")
    output = ""
    liste=["a", "e", "i", "o", "u", "å", "ø", "æ"]
    for count in range(0, len(a)):
        if a[count] in liste:
            output += a[count]
            continue
        if a[count] != " ":
            output += a[count] + "o" + a[count]
        else:
            output += a[count]

    print(output)

#calling the function
røverspråket()
            
