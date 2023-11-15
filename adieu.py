import inflect


def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            user_input = input("Name: ")
            names.append(user_input)
        except EOFError:
            print(f"Adieu, adieu, to {p.join(names)}")
            break


if __name__ == "__main__":
    main()
