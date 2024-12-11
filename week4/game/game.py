from random import randint
import sys

def main():
    l = get_level()
    n = randint(1, l)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            elif n > guess:
                print("Too small!")
            elif n < guess:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                continue
            return n
        except ValueError:
            pass
main()
