#!/usr/bin/env python3
def selectBiggest(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return a

# прямая передача значений
print(selectBiggest(1,2))
print(selectBiggest(3,2))
print(selectBiggest(2,2))

# передача переменных в качестве аргументов
x = 3
y = 4
print(selectBiggest(x,y))