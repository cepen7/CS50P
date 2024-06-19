import inflect

p = inflect.engine()

def main():
    names = askForName()
    say_adieu(names)


# creates a list of names
def askForName():
    names = []
    try:
        while True:
            name = input(str("Name: "))
            names.append(name)
    except EOFError:
        return names

# prints the greeting
def say_adieu(listOfNames):
    if len(listOfNames) == 1:
        print(f'Adieu, adieu, to {listOfNames[0]}')
    elif len(listOfNames) == 2:
        print(f'Adieu, adieu, to {listOfNames[0]} and {listOfNames[1]}')
    elif len(listOfNames) > 2:
        print('Adieu, adieu, to ' + p.join(listOfNames))

if __name__ == "__main__":
    main()
