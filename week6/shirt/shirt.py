import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
ex = [".jpg", ".jpeg", ".png"]
ex1 = os.path.splitext(sys.argv[1])[1]
ex2 = os.path.splitext(sys.argv[2])[1]
if ex1 not in ex:
    sys.exit("Invalid input")
elif ex2 not in ex:
    sys.exit("Invalid output")
elif ex1 != ex2:
    sys.exit("Input and output have different extensions")
try:
    image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    image = ImageOps.fit(image, shirt.size, Image.Resampling.BICUBIC, 0.0, (0.5, 0.5))
    image.paste(shirt,shirt)
    image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
