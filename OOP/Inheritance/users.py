class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):  # self refers to the current class instance
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
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy Birthday {self.first}! You just turned {self.age}"


class Moderator(User):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_active_mods(cls):
        return f"There are {cls.total_mods} active moderators."

    def remove_post(self):
        return f"{self.full_name} removed a post from the {self.community} community"


print(User.display_active_users())
u1 = User.from_string("Donovan,Mitchell,24")
u1 = User("Rudy", "Gobert", 27)
u1 = User("Joe", "Ingles", 32)
print(User.display_active_users())
jasmine = Moderator("Jasmine", "O'Connor", 61, 'Piano')
jasmine2 = Moderator("Jasmine", "O'Connor", 61, 'Guitar')
print(User.display_active_users())
print(Moderator.display_active_mods())


# print(jasmine.full_name())
# print(jasmine.community)
