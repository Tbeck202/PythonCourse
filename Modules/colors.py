import termcolor
# print(help(termcolor))
text = termcolor.colored("Fuck the Rockets!", color="yellow", on_color="on_magenta")
print(text)
termcolor.cprint("Go Jazz!", color="magenta", on_color="on_green")