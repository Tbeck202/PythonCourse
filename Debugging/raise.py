def colorize(text, color):
    colors = ('red', 'green', 'blue', 'indigo', 'violet')
    if type(text) is not str:
        raise TypeError("Ya gotta use strings, dawg!")
    elif color not in colors:
        raise ValueError(f"{color} is not a color, stupid!")
    print(f"Printed {text} in {color}")

colorize("hi", "red")
colorize("hi", "poop")


