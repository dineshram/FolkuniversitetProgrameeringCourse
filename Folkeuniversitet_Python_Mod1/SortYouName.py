__author__ = 'dram'

myName = input("Enter a name")
myDictionary = {}

for count in range(0, len(myName)):
    myDictionary[count] += 1

for count in range(0, len(myDictionary)):
    print("")
