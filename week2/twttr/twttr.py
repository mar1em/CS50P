s = input("Input: ")
for c in s:
    if c in ['a', 'A', 'e', 'E', 'I', 'i', 'o', 'O', 'U', 'u']:
        s = s.replace(c, '')

print(s)
