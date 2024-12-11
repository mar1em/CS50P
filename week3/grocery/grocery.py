d = {}
while True:
    try:
        item = input().upper()
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    except EOFError:
        break

for i in sorted(d):
    print(f"{d[i]} {i}")
