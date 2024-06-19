def main():
    full = input("Input: ")
    devowel(full)

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U" ]

def devowel(x):
    print("Output: ", end="")
    for y in x:
        if y not in vowels:
            print(y, end="")
    print()

main()


