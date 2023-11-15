from working import convert
import pytest


def main():
    test_convert()


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


if __name__ == "__main__":
    main()
