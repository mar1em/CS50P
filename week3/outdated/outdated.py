months = ["January","February","March","April","May", "June","July","August","September","October","November","December"]

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            if m > 12 or d > 31:
                continue
            print(f"{y}-{m:02}-{d:02}")
            break
        elif "," in date:
            month, d, y = date.split(" ")
            d = int(d.replace(',',''))
            if d > 31:
                continue
            if month in months:
                m = months.index(month) + 1
            if d > 31:
                continue
            print(f"{y}-{m:02}-{d:02}")
            break
        else:
            continue
    except ValueError:
        pass
