#!/usr/bin/env python3
number = 8
guess = int(input('Введите целое число:'))

if guess < number:
    print('Too small')
elif guess > number:
    print('Too big')
else:
    print('It is correct!')