from twttr import shorten


def main():
    test_shorten()


def test_shorten():
    assert shorten("TwItter") == "Twttr"
    assert shorten("twitter") == "twttr"
    assert shorten("tw1tter") == "tw1ttr"
    assert shorten("tw,tter") == "tw,ttr"


if __name__ == "__main__":
    main()
