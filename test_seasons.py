from seasons import counter
import pytest


def main():
    test_counter()


def test_counter():
    assert (
        counter("2022-06-25")
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    with pytest.raises(SystemExit):
        counter("January 1, 1999")


if __name__ == "__main__":
    main()
