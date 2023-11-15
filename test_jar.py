from jar import Jar
import pytest


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(12)


if __name__ == "__main__":
    main()
