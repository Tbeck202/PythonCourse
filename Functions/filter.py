# Retuns filter object which can be converted into other iterable types

l = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)  # [2, 4]

# ================================================

names = ['austin', 'penny', 'anthony', 'angel', 'billy']
a_names = list(filter(lambda x: x[0] == 'a', names))
name_list = ''
for name in a_names:
    if a_names.index(name) == len(a_names) - 1:
        name_list += "and " + name + "."
    else:
        name_list += name + ", "
print(f"The names that start with the letter 'a' are: {name_list}")
