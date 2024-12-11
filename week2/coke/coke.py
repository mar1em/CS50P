due = 50
while due > 0:
    print(f"Amount Due: {due}")
    i = int(input("Insert Coin: "))
    if i not in [5, 10, 25]:
        continue
    due -= i

if due == 0:
    print("Change Owed: 0")
else:
    print(f"Change Owed: {-1 * due}")
