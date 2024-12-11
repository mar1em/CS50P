def main():
    time = input("What time is it? ")
    t = convert(time)
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    h = float(hour)
    m = float(minute) / 60
    return (h + m)

if __name__ == "__main__":
    main()
