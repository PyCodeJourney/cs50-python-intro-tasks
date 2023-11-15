from pyfiglet import Figlet
import sys
from sys import argv
import random


def main():
    figlet = Figlet()
    fonts_list = figlet.getFonts()
    if len(sys.argv) == 1:
        figlet.setFont(font=random.choice(fonts_list))
    elif len(sys.argv) == 3 and (argv[1] == "-f" or argv[1] == "--font"):
        if argv[2] in figlet.getFonts():
            figlet.setFont(font=argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    user_input = input("Input: ")
    print(figlet.renderText(user_input))


if __name__ == "__main__":
    main()
