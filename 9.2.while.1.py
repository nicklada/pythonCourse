#!/usr/bin/env python3
number = 11

while True:
    guess = int(input('Введите целое число:'))
    if guess < number:
        print('Too small')
    elif guess > number:
         print('Too big')
    else:
        print('It is correct!')
        break
print('Well done!')