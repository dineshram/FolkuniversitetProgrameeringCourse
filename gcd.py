print("Please enter a number")
number = int(input())

sum = 0
sum1 = 0
i = 0
i1 = 0

while i <= number:
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    i = i + 1
        
for i1 in range(1, number):
    if i1 % 3 == 0 or i1 % 5 == 0:
        sum1 += i1

print(sum)
print(sum1)

