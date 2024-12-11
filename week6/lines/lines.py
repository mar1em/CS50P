import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")
try:
    n = 0
    with open(sys.argv[1]) as file:
        for line in file:
            l = line.strip()
            if l.startswith("#") == False and l != "":
                n += 1
    print(n)
except FileNotFoundError:
    sys.exit("File does not exist")
