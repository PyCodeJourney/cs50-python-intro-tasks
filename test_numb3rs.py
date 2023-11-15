from numb3rs import validate


def main():
    test_validate()


def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("255.256.256.256") == False


if __name__ == "__main__":
    main()
