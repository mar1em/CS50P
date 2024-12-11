s = input("camelCase: ")
for c in s:
    if c.isupper():
        s = s.replace(c, f'_{c.lower()}')
print(s)
