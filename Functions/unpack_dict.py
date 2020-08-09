def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {'first': 'Tyler', 'second': 'Alex'}

display_names(**names)


def add_mult_nums(a, b, c, **kwargs):
    print(a+b*c)
    if kwargs:
        print(kwargs)


data = dict(a=1, b=2, c=3)
more_data = dict(a=1, b=2, c=3, d=4, e="poop")
add_mult_nums(**data)
add_mult_nums(**more_data)
