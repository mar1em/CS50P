import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r'^([1-9]|1[0-2]) (AM|PM) to ([1-9]|1[0-2]) (AM|PM)$', s):
        h1 = int(matches.group(1))
        t1 = matches.group(2)
        h2 = int(matches.group(3))
        t2 = matches.group(4)
        if t1 == "AM" and h1 == 12:
            h1 = 0
        elif t1 == "PM" and h1 != 12:
            h1 += 12
        if t2 == "AM" and h2 == 12:
            h2 = 0
        elif t2 == "PM" and h2 != 12:
            h2 += 12
        return f"{h1:02}:00 to {h2:02}:00"
    elif matches := re.search(r'^([1-9]|1[0-2]):(\d\d) (AM|PM) to ([1-9]|1[0-2]):(\d\d) (AM|PM)$', s):
        h1 = int(matches.group(1))
        m1 = int(matches.group(2))
        t1 = matches.group(3)
        h2 = int(matches.group(4))
        m2 = int(matches.group(5))
        t2 = matches.group(6)
        if m1 >= 60 or m2 >= 60:
            raise ValueError
        if t1 == "AM" and h1 == 12:
            h1 = 0
        elif t1 == "PM" and h1 != 12:
            h1 += 12
        if t2 == "AM" and h2 == 12:
            h2 = 0
        elif t2 == "PM" and h2 != 12:
            h2 += 12
        return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
    elif matches := re.search(r'^([1-9]|1[0-2]):(\d\d) (AM|PM) to ([1-9]|1[0-2]) (AM|PM)$', s):
        h1 = int(matches.group(1))
        m1 = int(matches.group(2))
        t1 = matches.group(3)
        h2 = int(matches.group(4))
        t2 = matches.group(5)
        if m1 >= 60:
            raise ValueError
        if t1 == "AM" and h1 == 12:
            h1 = 0
        elif t1 == "PM" and h1 != 12:
            h1 += 12
        if t2 == "AM" and h2 == 12:
            h2 = 0
        elif t2 == "PM" and h2 != 12:
            h2 += 12
        return f"{h1:02}:{m1:02} to {h2:02}:00"
    elif matches := re.search(r'^([1-9]|1[0-2]) (AM|PM) to ([1-9]|1[0-2]):(\d\d) (AM|PM)$', s):
        h1 = int(matches.group(1))
        t1 = matches.group(2)
        h2 = int(matches.group(3))
        m2 = int(matches.group(4))
        t2 = matches.group(5)
        if m2 >= 60:
            raise ValueError
        if t1 == "AM" and h1 == 12:
            h1 = 0
        elif t1 == "PM" and h1 != 12:
            h1 += 12
        if t2 == "AM" and h2 == 12:
            h2 = 0
        elif t2 == "PM" and h2 != 12:
            h2 += 12
        return f"{h1:02}:00 to {h2:02}:{m2:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
