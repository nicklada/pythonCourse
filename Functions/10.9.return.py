#!/usr/bin/env python3
def balance(initial=100, *operations, cashback):
    balance = initial
    for operation in operations:
        balance -= operation
    balance += cashback
    return balance

print(balance(1000, 300, 2, 34, 29, 100, cashback=300))