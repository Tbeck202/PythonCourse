class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


jane = Human("Jane", "Goodall", 50)

print(f"{jane.first} is {jane.age} years old")
jane.age = 20
print(f"{jane.first} is {jane.age} years old")
print(jane.full_name)
