#!/usr/bin/env python3
def balance(initial=100, *operations, cashback):
    '''Рассчитывает баланс.

    Считает текущий баланс с учетом сумм операций и кешбека.'''
    balance = initial
    for operation in operations:
        balance -= operation
    balance += cashback
    print(balance)

balance(1000, 300, 2, 34, 29, 100, cashback=300)
#прочитаем строку документации функции balance атрибутом __doc__
print(balance.__doc__)
#функция help считывает атрибут __doc__ соответствующей функции 
# и аккуратно выводит его на экран
help(balance)