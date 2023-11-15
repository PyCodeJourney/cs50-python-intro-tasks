from plates import is_valid


def main():
    test_is_valid()


def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("3220") == False
    assert is_valid("CS50000000") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False


if __name__ == "__main__":
    main()
