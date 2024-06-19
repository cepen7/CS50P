def main():
    time = input("What time is it? ")
    mytime = convert(time)
    mytime = float(mytime)

    if 7 <= mytime <= 8:
        print("breakfast time")
    elif 12 <= mytime <= 13:
        print("lunch time")
    elif 18 <= mytime <= 19:
        print("dinner time")

# converts the entered time into a float rounded to 2 decimals
def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    mytime = hours + (minutes / 60)
    return (round(mytime, 2))

if __name__ == "__main__":
    main()
