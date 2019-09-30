from types import GeneratorType
# Итератор для удаления дубликатов
class Unique(object):
    IGNORE_CASE = False
    INDEX = 0
    OBJECTS = []
    PUSTOTA = []

    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs.keys():
            self.IGNORE_CASE = kwargs['ignore_case']
        if type(items == GeneratorType):
            self.OBJECTS = list(items)
        else:
            self.OBJECTS = items
        # self.ITEMS = len(items)

    def __next__(self):
        while True:  
            if self.INDEX == (len(self.OBJECTS) - 1):
                raise StopIteration
            self.INDEX += 1

            val = self.OBJECTS[self.INDEX]
            val2 = str(val).lower()
            if self.IGNORE_CASE:
                val = val2
            if val not in self.PUSTOTA:
                self.PUSTOTA.append(val)
                return val

    def __iter__(self):
        del self.PUSTOTA[:]
        self.INDEX = -1
        return self