from functools import wraps


def log_function_data(fn):
    # @wraps(fn) makes sure that the correct metadata presented when/if help() is called
    # otherwise, the wrapper() meta data will be presented
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM THE WRAPPER FUCTION"""
        print(f"You are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    """Adds two numbers together"""
    return x + y


print(add.__doc__)
print(add.__name__)
# help(add)
