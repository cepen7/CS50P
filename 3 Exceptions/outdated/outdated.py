def main():
    convert()
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


def convert():
    while True:
        try:
            usdate = input("Date: ").strip().title()
            if usdate[0].isdigit(): # for date format MM/DD/YYYY
                month, day, year = usdate.split("/")
                if 0 < int(month) <= 12 and 0 < int(day) <= 31:
                    print(f"{year}-{int(month):02}-{int(day):02}")
                    break
            else:
                for m in months:
                    if usdate.startswith(m): # for date format Month DD YYYY
                        comma = usdate.find(",")
                        day = int(usdate[comma -2: comma])
                        if 0 < day <= 31:
                            print(f"{usdate[comma+2:]}-{months[m]:02}-{day:02}")
                            break
                        else:
                            raise ValueError # if above cannot be printed, go again

                break
        except ValueError:
            pass
        except EOFError:
            break


main()

