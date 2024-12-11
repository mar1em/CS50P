from random import randint


def main():
    score = 0
    l = get_level()
    for i in range(10):
        x = generate_integer(l)
        y = generate_integer(l)
        eq = int(input(f"{x} + {y} = "))
        if eq == x + y:
            score += 1
        else:
            print("EEE")
            for __ in range(2):
                eq = input(f"{x} + {y} = ")
                if eq != x + y:
                    print("EEE")
                else:
                    score += 1
                    break
            print(f"{x} + {y} = {x+y}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                continue
            return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    else:
        return randint(100,999)

if __name__ == "__main__":
    main()
