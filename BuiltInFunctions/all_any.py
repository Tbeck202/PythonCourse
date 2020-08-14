nums = [2, 4, 6, 8]
nums2 = [2, 4, 6, 8, 9]

print(all([num % 2 == 0 for num in nums]))  # true
print(all([num % 2 == 0 for num in nums2]))  # false

names = ['Jim', 'John', 'Joe']
names2 = ['Jim', 'John', 'Joe', 'Bob']

if all([name[0] == "J" for name in names]):
    print("We got a bunch of J holes here!")

if not all([name[0] == 'J' for name in names2]):
    print("Well, at least one of ya ain't a J hole!")

print(any([num % 2 == 1 for num in nums]))  # False
print(any([num % 2 == 1 for num in nums2]))  # True
