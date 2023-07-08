#!/usr/bin/env python3
#функция tuple_print возвращает кортеж, который можно распаковать
def tuple_return():
    return (1, 3, 10, 'lada')

#распаковываем кортеж: gеременные element1 и element2 получают первые два элемента кортежа, 
# а переменная elements34 получает оставшиеся элементы в виде списка 
element1, element2, *elements34 = tuple_return()
print(*elements34)

#передаем кортеж в качестве аргумента, и 
# метод может использовать его значения внутри своего тела
class Printer:
    #метод принимает аргумент, который ожидается быть кортежем
    def tuple_print(t):
        for i in t:
            print('Печатаю элемент', i)

tuple1 = (1, 3, 10, 'lada')
printer = Printer()
Printer.tuple_print(tuple1)

#принимает кортеж
def tuple_print1(*t):
    for i in t:
        print('Печатаю элемент', i)

#принимает кортеж как единый элемент
tuple1 = (1, 3, 10, 'lada')
tuple_print1(tuple1)

#если хотим чтобы принимал как разные аргументы - 
# надо передавать как разные аргументы
tuple_print1(1, 3, 10, 'lada')

#может принимать 2 и более кортежа - каждый из них как единый аргумент
tuple2 = (2, 5, 11, 'grisha')
tuple_print1(tuple1, tuple2)