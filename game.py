import random


def main():
    while True:
        try:
            input_level = int(input("Level: "))
            if input_level > 0:
                break
            else:
                continue
        except ValueError:
            continue

    guessed_number = random.randint(1, input_level)

    while True:
        try:
            input_guess = int(input("Guess: "))
        except ValueError:
            continue
        if input_guess < guessed_number:
            print("Too small!")
        elif input_guess > guessed_number:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
