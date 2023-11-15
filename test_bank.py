from bank import value


def main():
    test_value()


def test_value():
    assert value("h") == 20
    assert value("hello") == 0
    assert value("What's up?") == 100
    assert value("Hi") == 20


if __name__ == "__main__":
    main()
