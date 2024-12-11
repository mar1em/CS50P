def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif "." in s or " " in s or "!" in s or "?" in s:
        return False
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    elif s.isalpha():
        return True
    else:
        for c in s:
            if c.isdigit():
                n = s.index(c)
                break
        if s[n] == "0":
            return False
        elif s[n:].isdigit() == False:
            return False
        return True


main()
