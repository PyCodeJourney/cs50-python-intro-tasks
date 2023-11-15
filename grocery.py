def main():
    grocery_list = {}
    while True:
        try:
            user_input = input().upper()
            if user_input in grocery_list:
                grocery_list[user_input] += 1
            else:
                grocery_list[user_input] = 1
        except EOFError:
            for key, value in sorted(grocery_list.items()):
                print(f"{value} {key}")
            break


if __name__ == "__main__":
    main()
