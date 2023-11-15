import re


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        user_input = input("Date: ").strip()
        if re.search(r"^\w+ \d+, \d+$", user_input):
            for m in months:
                if m in user_input:
                    user_input = user_input.replace(m, str(months.index(m) + 1))
                    data = re.search(r"^(\d+)+ (\d+)+, (\d+)+$", user_input)
                    month = data.group(1)
                    day = data.group(2)
                    year = data.group(3)
                    break
        elif re.search(r"^\d+/\d+/\d+$", user_input):
            data = re.search(r"^(\d+)+/(\d+)+/(\d+)+$", user_input)
            month = data.group(1)
            day = data.group(2)
            year = data.group(3)
        else:
            continue
        try:
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            continue
        if 1 < month <= 12 and 1 < day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue


if __name__ == "__main__":
    main()
