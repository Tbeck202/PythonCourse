# num = 1
# while num < 10:
#     print("\U0001f600" * num)
#     num += 1

# for count in range(1, 10):
#     print("\U0001f600" * count)

# for count in range(1, 20, 2):
#     space = " "
#     space_count = 1
#     print(space * space_count + "\U0001f600" * count)
#     space_count += 1

count = 1
space_count = 18
while count < 20:
    space = " " * space_count
    if count % 2 != 0:
        print(space + "\U0001f600" * count)

    elif count == 19:
        print("\U0001f600" * count)
    count += 1
    space_count -= 1
