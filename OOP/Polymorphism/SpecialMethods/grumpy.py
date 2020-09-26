class GrumpyDict(dict):
    def __repr__(self):
        print("WOULDN'T YOU LIKE TO KNOW!")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANTED {key}?? WELL TOO BAD!!")

    def __setitem__(self, key, value):
        print('WHY YOU ALWAYS GOTTA CHANGE STUFF??')
        print('UGH... FINE!')
        super().__setitem__(key, value)

    def __contains__(self, items):
        print('DON\'T BOTHER ME!')
        return False


data = GrumpyDict({'first': 'Tom', 'animal': 'cat'})
print(data)
data['city']
data['city'] = 'Tokyo'
print(data)
print('city' in data)
