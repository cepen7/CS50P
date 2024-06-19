import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        lets_count(0,10)
    elif level == 2:
        lets_count(10,100)
    elif level == 3:
        lets_count(100,1000)


def lets_count(start, end):
    score = 0
    for i in range(10):
        x = random.randrange(start, end)
        y = random.randrange(start, end)
        for j in range(3):
            answer = int(input(f'{x} + {y} = '))
            correctResult = x + y
            if answer != correctResult:
                print('EEE')
                if j == 2:
                    print(f'{x} + {y} = {x+y}')
            elif answer == correctResult:
                score += 1
                break
    print('Score:', score)


if __name__ == "__main__":
    main()
