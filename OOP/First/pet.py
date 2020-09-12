class Pet:

    allowed = ['cat', 'dog', 'fish', 'rat'] # class attribute

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet!")
        self.species = species

cat = Pet("Zorro", "cat")
dog = Pet("Lua", "dog")
tiger = Pet("Tony", "tiger")

print(cat)
print(dog)
print(tiger)