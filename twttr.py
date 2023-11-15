def main():
    user_input = input("Input: ").strip()
    print(replaceVowels(user_input, ""))


def replaceVowels(input, replacer):
    vowels = "AEIOUaeiou"
    for c in vowels:
        input = input.replace(c, replacer)

    return input


if __name__ == "__main__":
    main()
