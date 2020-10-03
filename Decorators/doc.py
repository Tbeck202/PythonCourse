def be_polite(fn):
    def wrapper():
        print("Nice to meet you!")
        fn()
        print("Have a great day!")
    return wrapper


@be_polite
def greet():
    print("My name is Tyler.")


@be_polite
def rage():
    print('I hate you!')


# with the @be_polite decorator, we dont have to assign the function to a variable. We just call the function, in this case greet() & polite_rage()
# greet = be_polite(greet)
# polite_rage = be_polite(rage)

greet()
rage()
