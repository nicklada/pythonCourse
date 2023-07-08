#!/usr/bin/env python3
def balance(initial=100, *operations, cashback):
    balance = initial
    for operation in operations:
        balance -= operation
    balance += cashback
    print(balance)

balance(1000, 300, 2, 34, 29, 100, cashback=300)

#Если для ключевых аргументов не указано значение по умолчанию, 
#и оно не передано при вызове, 
# обращение к функции вызовет ошибку
balance(1000, 300, 2, 34, 29, 100, 300)