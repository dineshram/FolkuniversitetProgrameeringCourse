eval = int(input("Enter the number : "))
i = 0
sum = 0

for i in range(1, eval):
    if i % 3 == 0:
        sum += i
        continue
    if i % 5 == 0:
        sum += i
        continue

print(sum)


