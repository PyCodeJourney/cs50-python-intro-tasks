from fuel import convert, gauge
import pytest


def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("99/100") == 99
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(75) == "75%"


if __name__ == "__main__":
    main()
