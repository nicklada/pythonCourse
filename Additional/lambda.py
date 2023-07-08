#!/usr/bin/env python3
#простая lambda функция 
#lambda arguments: expression
add = lambda x, y: x - y
print(add(5,4))

#сортировка с помощью lambda функции
points = [ { 'x' : 2, 'y' : 3 }, { 'x' : 4, 'y' : 1 } ] 
newpoints = points[:]
#сортирует список points по возрастанию значению ключа 'y' в каждом словаре, 
#используя лямбда-функцию в качестве ключа сортировки
newpoints.sort(key=lambda i : i['y'])
print(newpoints)

