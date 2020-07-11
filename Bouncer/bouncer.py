print("How old are you?")
age = input()
if age:
    age_num = int(age)
    if age_num < 18:
        print("You're too young! Go home.")
    elif age_num >= 18 and age_num < 21:
        print("Come on in! But you're not allowed to drink.")
    else:
        print("Come in and have a drink!")
else:
    print("Ya gotta enter something, ding dong!")
