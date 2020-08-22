# print(len('Donovan Mitchell'))


class SpecialList:
    def __init__(self, data):
        self.__data__ = data

    def __len__(self):
        return self.__data__.__len__() + 5


l1 = SpecialList([1, 40, 30, 100])
l2 = SpecialList([])
print(len(l1))
print(len(l2))
