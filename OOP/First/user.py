class User:
    def __init__(self, first, last, age): # self refers to the current class instance
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def info(self):
        return f"{user1.first} {user1.last} is {user1.age} years old!"

    def initials(self):
        return f"{self.first[0].upper()}.{self.last[0].upper()}."

    def likes(self, thing):
        return f"{self.first} likes {thing}!"

    def is_senior(self):
        return self.age >= 62

    def birthday(self):
        self.age += 1
        return f"Happy Birthday {self.first}! You just turned {self.age}"


user1 = User("Tyler", "Beck", 37) # instantiating classes
user2 = User("Alex", "Linsley", 31) # instantiating classes
user3 = User("John", "Johnson", 66)

print(user1.full_name())
print(user1.info())
print(user1.birthday())
print(user1.info())
print(user2.initials())
print(user2.likes("wine"))
print(user1.is_senior())
print(user3.is_senior())



# print(f"{user1.first} {user1.last} is {user1.age} years old!")
# print(f"{user2.first} {user2.last} is {user2.age} years old!")