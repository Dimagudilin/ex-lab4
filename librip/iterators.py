from types import GeneratorType
# Итератор для удаления дубликатов
class Unique(object):
    IGNORE_CASE = False
    INDEX = 0
    OBJECTS = []
    VOID = []

    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs.keys(): #Проверка на регистр
            self.IGNORE_CASE = kwargs['ignore_case']
        if type(items == GeneratorType): #Для генератора
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
            if self.IGNORE_CASE: #Если регистр игнорируется, то ставим второе значение
                val = val2
            if val not in self.VOID: #Если не находится значение в списке, туда его добавляем
                self.VOID.append(val)
                return val

    def __iter__(self): #Возвращает итератор для объекта
        del self.VOID[:]
        self.INDEX = -1
        return self