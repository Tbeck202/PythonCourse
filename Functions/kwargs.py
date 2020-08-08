def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


fav_colors(tyler="green")
fav_colors(bob="blue", alex="turquoise")


def greeting(**kwargs):
    if "Alex" in kwargs and kwargs['Alex'] == "special":
        print("Alex gets a special greeting")
    elif "Tyler" in kwargs:
        print(f"{kwargs['Tyler']} Tyler")
    else:
        print("Who the eff are you??")


greeting(Alex="special")
greeting(Tyler="Hi")
greeting(John="whatever")
