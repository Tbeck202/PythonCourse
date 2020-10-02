from random import choice


def make_laugh_func(person):
    def get_laugh():
        laugh = choice(('HAHAHAHA', 'LOL', 'tee hee'))
        return f"{laugh} {person}!"

    return get_laugh


laugh = make_laugh_func('Linda')
print(laugh())
