from random import randint


def main():
    fails = 0
    count = 0
    score = 0
    level = get_level()

    while count < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            answer = x + y
            try:
                user_answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                fails += 1
            if user_answer == answer:
                count += 1
                score += 1
                fails = 0
                break
            else:
                print("EEE")
                fails += 1
            if fails == 3:
                print(f"{x} + {y} = {answer}")
                count += 1
                fails = 0
                break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        number = randint(0, 9)
    elif level == 2:
        number = randint(10, 99)
    elif level == 3:
        number = randint(100, 999)
    return number


if __name__ == "__main__":
    main()
