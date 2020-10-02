
def nums():
    for num in range(1, 10):
        yield num


gen1 = nums()
print(gen1)

gen2 = (num for num in range(1, 10))
print(gen2)
