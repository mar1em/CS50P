from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    dob = input("Date of Birth: ")
    dt = get_date(dob)
    duree = date.today() - dt
    minutes = duree.days * 24 * 60
    words = p.number_to_words(minutes, andword="").capitalize()
    print(f"{words} minutes")
def get_date(d):
    if matches := re.search(r'^(\d\d\d\d)-(\d\d)-(\d\d)$', d):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
        return date(year, month, day)
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
