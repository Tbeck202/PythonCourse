nums = [2, 4, 6, 8, 10]

doubles = map(lambda x: x * 2, nums)
# print(doubles) won't print. just prints that this is a map object: <map object at 0x7fd235a2ff10>
print(doubles)
print(list(doubles))  # prints a list: [4, 8, 12, 16, 20]

# ================================================================
people = ['Bill', 'Bob', 'Gina', 'Jill']

peeps = map(lambda name: name.upper(), people)
print(list(peeps))  # ['BILL', 'BOB', 'GINA', 'JILL']

# ================================================================

names = [
    {'first': 'Tyler', 'last': 'Beck'},
    {'first': 'Alex', 'last': 'Linsley'},
    {'first': 'Bill', 'last': 'Billerson'}
]

first_names = list(map(lambda x: x['first'], names))
print(first_names)  # ['Tyler', 'Alex', 'Bill']
