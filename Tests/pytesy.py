#!/usr/bin/env python3
import pytest

def balance(initial=100, *operations, cashback):
    balance = initial
    for operation in operations:
        balance -= operation
    if balance <= 100:
        cashback == 0
    else:
        balance += cashback
    return balance

#balance(1000, 300, 2, 34, 29, 100, cashback=300)

#Если для ключевых аргументов не указано значение по умолчанию, 
#и оно не передано при вызове, 
# обращение к функции вызовет ошибку
#balance(1000, 300, 2, 34, 29, 100, 300)

def test_positive():
    actual = balance(1000, 300, 2, cashback=300)
    expected = 998.0
    assert actual == expected

def test_negative():
    with pytest.raises(TypeError):
        balance(1000, 300, 2, 300)

@pytest.mark.parametrize('initial, operations, expected', [
    (200, 30, 180.0),
    (50, 70, -20),
    (10, -150, 170) ])

def test_with_params(initial, operations, expected):
    back = 10
    result = balance(initial, operations, cashback = back)
    assert result == expected

