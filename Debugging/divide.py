def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError as err:
        print("Ya can't divide by 0 dum dum!")
        print(err)
    except TypeError as err:
        print("Both 'a' and 'b' must be either int or float.")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

print(divide(1,2))
print(divide(1,0))
print(divide(1,'a'))