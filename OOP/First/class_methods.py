class User:
    active_users = 0 

    @classmethod
    def display_active_users(cls):
        return f"There are {cls.active_users} active users."
        
    @classmethod
    def from_string(cls, data_str):
        first,last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age): # self refers to the current class instance
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out!"

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def info(self):
        return f"{self.first} {self.last} is {self.age} years old!"

    def initials(self):
        return f"{self.first[0].upper()}.{self.last[0].upper()}."

    def likes(self, thing):
        return f"{self.first} likes {thing}!"

    def is_senior(self):
        return self.age >= 62

    def birthday(self):
        self.age += 1
        return f"Happy Birthday {self.first}! You just turned {self.age}"

don = User.from_string("Donovan,Mitchell,24")
print(don.info())

# user1 = User("Tyler", "Beck", 37) # instantiating classes
# user2 = User("Alex", "Linsley", 31) # instantiating classes

# print(User.display_active_users())
# user3 = User("John", "Johnson", 66)
# print(User.display_active_users())
# user3.logout()
# print(User.display_active_users())

# print(user1.full_name())
# print(user1.info())
# print(user1.birthday())
# print(user1.info())
# print(user2.initials())
# print(user2.likes("wine"))
# print(user1.is_senior())
# print(user3.is_senior())

# print(User.active_users)
# user1 = User("Tyler", "Beck", 37) # instantiating classes
# user2 = User("Alex", "Linsley", 31) # instantiating classes
# user3 = User("John", "Johnson", 66)
# print(User.active_users)
# print(user1.logout())
# print(User.active_users)


# print(f"{user1.first} {user1.last} is {user1.age} years old!")
# print(f"{user2.first} {user2.last} is {user2.age} years old!")