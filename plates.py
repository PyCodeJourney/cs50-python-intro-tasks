import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not start_pattern_check(s):
        return False
    if not length_check(s):
        return False
    if not zero_check(s):
        return False
    if not digits_pattern_check(s):
        return False
    if not punctuation_check(s):
        return False
    return True


def start_pattern_check(s):
    if not s[0:2].isalpha():
        return False
    else:
        return True


def length_check(s):
    str_length = len(s)
    if str_length <= 2 or str_length > 6:
        return False
    else:
        return True


def zero_check(s):
    for char in s:
        if char.isdigit():
            if char == "0":
                return False
            else:
                return True
    return True


def digits_pattern_check(s):
    found_digit = False
    for char in s:
        if char.isdigit():
            if found_digit:
                continue
            else:
                found_digit = True
        elif found_digit:
            return False
    return True


def punctuation_check(s):
    for char in s:
        if char in string.punctuation:
            return False
    return True


if __name__ == "__main__":
    main()
