def main():
    while True:
        user_input = input("Fraction: ")
        try:
            x, y = user_input.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                raise ValueError
        except ValueError:
            continue
        try:
            fuel_percentage = round(x / y * 100)
        except ZeroDivisionError:
            continue
        if fuel_percentage >= 99:
            print("F")
        elif fuel_percentage <= 1:
            print("E")
        else:
            print(f"{fuel_percentage}%")
        break


if __name__ == "__main__":
    main()
