def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total


nums = (1, 2, 3, 4, 5, 6)
print(sum_all_values(*nums))
