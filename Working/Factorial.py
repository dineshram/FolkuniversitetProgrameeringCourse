#Factorial calculation

factorial = 1
num = int(input("Enter a number whose factorial you want to calculate : "))
for i in range(num, 1, -1):
    factorial*=i

print("Factorial of ", num, " is ", factorial)
