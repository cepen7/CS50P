def main():
    s = input("camelCase: ")
    print("snake_case: ", end="")
    convert(s)

# puts underscore in front of every uppercase and turns all lowercase
def convert(n):
    for char in n:
        if char.istitle():
            print("_" + char.lower(), end="")
        else:
            print(char, end="")
    print()

main()