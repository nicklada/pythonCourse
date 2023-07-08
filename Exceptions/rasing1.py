#!/usr/bin/env python3

class ShortLength(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    data = input('Введите что-то: ')
    if len(data)<3:
        raise ShortLength(len(data), 3)
except ShortLength as e:
    print('ShortInputException: Длина введённой строки -- {0}; \
ожидалось, как минимум, {1}'.format(e.length, e.atleast))
else:
    print(data)