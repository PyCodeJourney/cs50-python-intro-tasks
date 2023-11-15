def main():
    user_input = input("Expression: ").strip()
    x, y, z = user_input.split(" ")
    x = int(x)
    z = int(z)
    if y == "/" and z != 0:
        print(float(x / z))
    elif y == "+":
        print(float(x + z))
    elif y == "-":
        print(float(x - z))
    elif y == "*":
        print(float(x * z))


if __name__ == "__main__":
    main()
