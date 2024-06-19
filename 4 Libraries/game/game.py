import random


def main():
    n = get_number()
    guess(n)


def get_number():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            continue

def guess(x):
    winningNumber = random.randrange(1, x + 1)
    while True:
        try:
            guessNumber = int(input("Guess: "))
            if guessNumber <= 0:
                continue
            elif guessNumber < winningNumber:
                print("Too small!")
            elif guessNumber > winningNumber:
                print("Too large!")
            elif guessNumber == winningNumber:
                print("Just right!")
                break
        except ValueError:
            continue


if __name__ == "__main__":
    main()
