s = input()
result = ''

l = ['a', 'e', 'i', 'o', 'u']
for i in range(0, len(s)):
    if(s[i] in l):
        result += s[i]
        continue
    result += s[i] + 'o' + s[i]

print(result)
    
