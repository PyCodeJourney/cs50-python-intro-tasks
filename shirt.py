import sys
from PIL import Image, ImageOps


def main():
    valid_file_exstensions = (".jpg", ".jpeg", ".png")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(valid_file_exstensions) or not sys.argv[2].endswith(
        valid_file_exstensions
    ):
        sys.exit("Not an Image")
    elif sys.argv[1][-3:-1] != sys.argv[2][-3:-1]:
        sys.exit("Input and output have different extensions")
    try:
        with Image.open(sys.argv[1]) as input_image, Image.open("shirt.png") as shirt:
            croppedImage = ImageOps.fit(input_image, shirt.size)
            croppedImage.paste(shirt, shirt)
            croppedImage.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
