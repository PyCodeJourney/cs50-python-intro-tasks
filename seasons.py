from datetime import date
import inflect
import sys


def main():
    print(counter(input("Date of Birth: ")))


def counter(s):
    try:
        user_birth = date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid data")
    time_since = date.today() - user_birth
    minutes_since = int(time_since.total_seconds() / 60)
    p = inflect.engine()
    return f'{p.number_to_words(minutes_since, andword="").capitalize()} minutes'


if __name__ == "__main__":
    main()
