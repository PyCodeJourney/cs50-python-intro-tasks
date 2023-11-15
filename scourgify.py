import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        try:
            with open(sys.argv[1], "r") as r_file, open(sys.argv[2], "w") as w_file:
                reader = csv.DictReader(r_file)
                writter = csv.DictWriter(w_file, fieldnames=["first", "last", "house"])
                writter.writeheader()
                for row in reader:
                    name = row["name"].split(", ")
                    writter.writerow(
                        {"first": name[1], "last": name[0], "house": row["house"]}
                    )
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
