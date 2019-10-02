from librip.gen import gen_random
from librip.iterators import Unique
# Реализация задания 2

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
print(list(Unique(data))) #будет последовательно возвращать только 1 и 2

data = gen_random(1, 3, 10)
print(list(Unique(gen_random(1, 3, 10)))) #будет последовательно возвращать только 1, 2 и 3

data = ["a", "A", "b", "B"]
print(list(Unique(data))) #будет последовательно возвращать только a, A, b, B

data = ["a", "A", "b", "B"]
print(list(Unique(data, ignore_case=True))) #будет последовательно возвращать только a, b