def sum_digits(n):
    s  = 0
    while n:
        s += n % 10
        n /= 10
    return s

def sum_digits2(n):
    s = 0
    while n:
        n, remainder = divmod(n, 10)
        s += remainder
    return s

def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n / 10
   return r

print("sum of digits of 1206 is ", int(sum_digits(1206)))
print("sum of digits of 37898 is ", int(sum_digits2(37898)))
print("sum of digits of 5555 is ", int(sum_digits3(5555)))
