import re

def main():
    print(count(input("Text: ")))


def count(s):
    n = 0
    matches = re.findall(r"\bum(\b|\W)", s, re.IGNORECASE)
    for match in matches:
        n += 1
    return n

if __name__ == "__main__":
    main()
