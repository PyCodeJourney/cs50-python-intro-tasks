def main():
    user_input = input()
    print(convert(user_input))

def convert(user_input):
    user_input = user_input.replace(":)", "🙂")
    user_input = user_input.replace(":(", "🙁")
    return user_input

if __name__ == "__main__":
    main()