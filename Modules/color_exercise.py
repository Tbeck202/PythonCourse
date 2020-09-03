import termcolor
from pyfiglet import Figlet

f = Figlet(font='graffiti')

while True:
    text = input("What message do you want to print? \n")
    print("What color do you want the text?")
    color = input("Green, Magenta, Blue, Cyan, Red or Yellow? \n").lower()

    try:
        termcolor.cprint(f.renderText(text), color=color)
        break
    except KeyError:
        print("Ya gotta use one of the colors in the color list!")
