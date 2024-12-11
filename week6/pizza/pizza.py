from tabulate import tabulate
import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
try:
    t = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            t.append(row)
    print(tabulate(t[1:], t[0], tablefmt = "grid"))

except FileNotFoundError:
    sys.exit("File does not exost")
