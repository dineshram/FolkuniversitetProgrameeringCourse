import random

print("Welcome to Rock, Paper and Scissors !!!")
# TIP : How to check if the entered value is an integer
# TIP : How to check if the entered value is a positive integer
numberOfTurns = int(input("How many points are required for a win? "))
if(numberOfTurns <= 0):
    print("The point to win should be a number greater than 0 ")
    numberOfTurns = int(input("Please enter the number of points required for a win "))
#TIP : What if I enter the numberOfTurns incorrectly again !
#TIP : Solve this with a do while loop : while(numberOfTurns <= 0)

validOptions = ['r', 'p', 's']
scoreHuman = 0
scoreComputer = 0
currentRound = 1

while True:
    print("Current Round = ", currentRound)
    option = input("Choose : Rock(r), Paper(p) or Scissors(s) ")
    if(option == 'r'):
        print("Human : rock")
    elif(option == 'p'):
        print("Human : paper")
    elif(option == 's'):
        print("Human : scissors")
    else:
        print("Please select the correct option")
        continue

    optionC = validOptions[random.randrange(len(validOptions))]
    if(optionC == 'r'):
        print("Computer : rock")
    elif(optionC == 'p'):
        print("Computer : paper")
    elif(optionC == 's'):
        print("Computer : scissors")
    if(option == optionC):
        print("Tied round !!")
        print("Score : Human = ", scoreHuman, "Computer = ", scoreComputer)
        continue

    if(option == 'r'):
        if(optionC == 'p'):
            print("Computer Wins !!")
            scoreComputer += 1
            print("Score : Human = ", scoreHuman, "Computer = ", scoreComputer)
        else:
            print("Human Wins !!")
            scoreHuman += 1
            print("Score : Human = ", scoreHuman, "Computer = ", scoreComputer)
    elif(option == 'p'):
        if(optionC == 's'):
            print("Computer Wins !!")
            scoreComputer += 1
            print("Score : Human = ", scoreHuman, "Computer = ", scoreComputer)
        else:
            print("Human Wins !!")
            scoreHuman += 1
            print("Score : Human = ", scoreHuman, "Computer = ", scoreComputer)
    elif(option == 's'):
        if(optionC == 'r'):
            print("Computer Wins !!")
            scoreComputer += 1
            print("Score : Human = ", scoreHuman, "Computer = ", scoreComputer)
        else:
            print("Human Wins !!")
            scoreHuman += 1
            print("Score : Human = ", scoreHuman, "Computer = ", scoreComputer)

    if(scoreHuman == numberOfTurns or scoreComputer == numberOfTurns):
        break

    currentRound += 1
    print("----------New Round-----------")
