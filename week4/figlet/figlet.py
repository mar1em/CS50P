from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3 and (sys.argv[1] != "-f" and sys.argv[1] != "--font"):
    sys.argv("Invalid usage")
elif len(sys.argv) == 3 and sys.argv[2] not in fonts:
    sys.exit("Invalid usage")

s = input("Input: ")

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
else:
    figlet.setFont(font=sys.argv[2])

print(figlet.renderText(s))
