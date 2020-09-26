from copy import copy  # used to in the __mult__() method because otherwise each new object would be a reference to the same object. This module creates a new object in memory for each new instance


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}. Age: {self.age}"

    def __len__(self):
        return self.age

    # the "+" sign calls this special __add__ method
    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        raise TypeError("You can't add those together!")

    # the "*" sign calls this special __mul__ method
    def __mul__(self, other):
        if isinstance(other, int):
            return[copy(self) for i in range(other)]
        raise TypeError("You can't multiply those together!")


j = Human("Jenny", "Larson", 47)
k = Human("Kevin", "Jones", 49)

# print(j)
# print(len(j))

# print(j + k)

baby = j + k
baby.first = 'Timmy'
print(baby)

triplets = j * 3
triplets[1].first = 'Jessica'
print(triplets)
for t in triplets:
    print(t.first)

triplets2 = (k + j) * 3

print(triplets2)
