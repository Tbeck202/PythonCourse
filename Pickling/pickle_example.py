import pickle

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species='Cat')
        self.breed = breed
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"


zorro = Cat('Zorro','Tabby','String')

with open('pets.pickle', 'wb') as file:
    pickle.dump(zorro, file)


def un_pickle(target):
    with open(target, 'rb') as file:
        un_pickled = pickle.load(file)
        print(un_pickled)

# un_pickle('pets.pickle')