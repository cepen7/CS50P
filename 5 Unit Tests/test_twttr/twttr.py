def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")



def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U" ]
    devoweledWord = ""
    for y in word:
        if y not in vowels:
            devoweledWord += y
    return devoweledWord


if __name__ == "__main__":
    main()
