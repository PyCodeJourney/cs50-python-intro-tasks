import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(
        r"^(1[0-2]|0?[1-9]):([0-5][0-9]) (\w{2}) to (1[0-2]|0?[1-9]):([0-5][0-9]) (\w{2})$",
        s,
    ):
        h1, m1, am_pm1, h2, m2, am_pm2 = matches.groups()
        h1 = int(h1)
        h2 = int(h2)

        return f"{continental_time_format(h1,am_pm1):02d}:{m1} to {continental_time_format(h2,am_pm2):02d}:{m2}"

    elif matches := re.search(
        r"^(1[0-2]|0?[1-9]) (\w{2}) to (1[0-2]|0?[1-9]) (\w{2})$",
        s,
    ):
        h1, am_pm1, h2, am_pm2 = matches.groups()
        h1 = int(h1)
        h2 = int(h2)

        return f"{continental_time_format(h1,am_pm1):02d}:00 to {continental_time_format(h2,am_pm2):02d}:00"

    else:
        raise ValueError


def continental_time_format(h, am_pm):
    if am_pm == "PM" and h != 12:
        h += 12
    elif am_pm == "AM" and h == 12:
        h = 0
    return h


if __name__ == "__main__":
    main()
