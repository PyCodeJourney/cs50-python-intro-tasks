import requests
import sys


def main():
    if len(sys.argv) == 2:
        if is_float(sys.argv[1]):
            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            price = r.json()
            amount = float(sys.argv[1]) * price["bpi"]["USD"]["rate_float"]
            print(f"${amount:,.4f}")
        else:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argumen")


def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
