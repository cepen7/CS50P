from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 1:
    s = input("Input: ")
    randomFont = random.choice(fonts)
    figlet.setFont(font=randomFont)
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            r = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(r))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
