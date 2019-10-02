

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
#data = sorted(data, key=abs())
data = sorted(data, key=lambda x: abs(x)) #key- функция, вызываемая на каждом элементе перед сравнением, то есть функция модуля
print(data)
