def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    for c in word:
        if c in ['A','a','E','e','I','i','O','o','U','u']:
            word = word.replace(c, '')
    return word

if __name__ == "__main__":
    main()
