import random

def field(items, *args):
    assert len(args) > 0    # Проверка на ошибку
    if len(args) == 1: #Если передан один аргумент
        for i in items:
            for a in args:
                yield i[a]
    else: # Для нескольких аргументов
        for i in items:  # Для каждого словаря
            dict = {}  # Создаем новый словарь
            for arg in args:
                if arg in i is not None:
                    dict[arg] = i[arg]  # Заполняем словарь
            if len(dict) > 0 and len(args) > 1:
                yield dict


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for _ in range(num_count):
        yield random.randint(begin, end)