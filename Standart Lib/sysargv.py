#!/usr/bin/env python3
import sys

try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]

except IndexError:
    print('Вы ввели меньше 3х аргументов')

else:
    print('Вы запустили скрипт со следующими аргументами: ', arg1, arg2, arg3)

