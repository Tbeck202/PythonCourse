# *args will collect all arguments passed in and put them in a tuple
def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total


# print(sum_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9))  # = 45

# ==========================================================================
def ensure_info(*args):
    if "Tyler" in args and "Beck" in args:
        print("Welcome back, Tyler")
    else:
        print("Who the FUCK are you??")


ensure_info("Tyler", "Beck", 1, True)
ensure_info("Tyler", 1, True)
