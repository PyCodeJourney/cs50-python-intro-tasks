def main():
    user_input = input("What time is it? ").strip()
    hours = convert(user_input)
    if 7.00 <= hours <= 8.00:
        print("breakfast time")
    elif 12.00 <= hours <= 13.00:
        print("lunch time")
    elif 18.00 <= hours <= 19.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) * 1 / 60
    return float(hours + minutes)


if __name__ == "__main__":
    main()
