import random

print("guessing a number...........")

number = random.randint(1, 20)
#print("I guessed " + str(number))

numberOfGuesses = 0
print("please guess a numner :")

while numberOfGuesses < 5:
    guess = int(input())
    numberOfGuesses += 1

    if guess < number:
        print("Please guess a higher number")

    if guess > number:
        print("Please guess a lower number")

    if guess == number:
        break

if guess == number:
    print("Hurrah! You guessed correctly in " + str(numberOfGuesses) + " chances ")

if guess != number:
    print("Sorry ! all your guesses were incorrect")
    print("The correct number was " + str(number))

