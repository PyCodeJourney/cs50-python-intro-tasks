import sys


def main():
    count = 0
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    line = line.lstrip()
                    if line.startswith("#") or len(line) == 0:
                        continue
                    else:
                        count += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
    print(count)


if __name__ == "__main__":
    main()
