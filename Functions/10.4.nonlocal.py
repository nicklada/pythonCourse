#!/usr/bin/env python3
x = 10

def outerfunc():
    #локальная переменная x - переопределит x которая за пределами функции
    x = 2
    print('x равно', x)

    def func_inner():
        #находится ни в локальной области видимости, 
        # ни в глобальной области видимости 
        nonlocal x
        x = 5

    func_inner()
    print('Локальное х сменилось на', x)

outerfunc()