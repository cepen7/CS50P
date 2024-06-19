def main():
    a = convert("Fraction: ")
    if 0 <= a <= 1:
        print("E")
    elif 1 < a < 99:
        print(f"{a:.0f}%")
    elif 99 <= a <= 100:
        print("F")
        
def convert(prompt):
    while True:
        try:
            fraction = input(prompt)
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x <= y:
                return ((x/y)*100)
            else:
                pass
        except ZeroDivisionError:
            pass
        except ValueError:
            pass

main()
