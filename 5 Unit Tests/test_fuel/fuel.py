import sys

def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x <= y:
            return int(((x/y)*100))
        elif y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError


def gauge(a):
    if 0 <= a <= 1:
        return("E")
    elif 1 < a < 99:
        return(f"{a}%")
    elif 99 <= a <= 100:
        return("F")

if __name__ == "__main__":
    main()
