print("Welcome to palindromes")

s1 = int(input("Enter a word:"))

print("Checking if input is a palindrome....")

counter = 0
s2 = 0

for counter in range (1, s1):
    s2 = s2 + s1[counter]

print(s2)

