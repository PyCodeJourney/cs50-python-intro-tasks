from um import count


def main():
    test_count()


def test_count():
    assert count("yummy") == 0
    assert count("Um, thanks for the album.") == 1


if __name__ == "__main__":
    main()
