class GrumpyDict(dict):
    def __repr__(self):
        # super() will call the dict methods that were passed into GrumpyDict
        return super().__repr__()

    def __missing__(self, key):
        print(f"Oh, you want {key}? Well tough shit! It aint here.")

    def __setitem__(self, key, value):
        print("Fine, I'll change the dictionary.")
        super().__setitem__(key, value)


data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['color']
data['city'] = 'Tokyo'
print(data)
