def shout(fn):
    # the *args and **kwargs make it so the wrapper function can work with any number of arguments
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}."


@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."


print(greet('Tyler'))
print(order('Cheeseburger', 'Fries'))
