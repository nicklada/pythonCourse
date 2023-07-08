#!/usr/bin/env python3
#создаем список
fruitlist = ['яблоки', 'манго', 'морковь', 'бананы']

#получаем элемент последовательности по индексу
print('Элемент 0 - ', fruitlist[0])
print('Элемент 1 - ', fruitlist[1])
print('Элемент 2 - ', fruitlist[2])
print('Элемент 3 - ', fruitlist[3])
print('Элемент 2 - ', fruitlist[-1])
print('Элемент 3 - ', fruitlist[-2])

berry = 'strawberry'

#получаем элемент строки по индексу
print('Элемент 0 - ', berry[0])

#вырезки
print('Элементы с 1 по 3: ', fruitlist[1:3])
print('Элементы с 2 до конца ', fruitlist[2:])
print('Элементы с 1 по -1: ', fruitlist[1:-1])
print('Элементы с начала до конца: ', fruitlist[:])
print('Символы с 1 по 3: ', berry[1:3])
print('Символы с 2 до конца: ', berry[2:])
print('Символы с 1 по -1: ', berry[1:-1])
print('Символы с начала до конца: ', berry[:])

#указать шаг
#шаг = 1 = печатать каждый элемент
print(fruitlist[::1])
#шаг = 2 = печатать каждый второй элемент
print(fruitlist[::2])
#шаг = -1 = печатать список с конца
print(fruitlist[::-1])

