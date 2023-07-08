#!/usr/bin/env python3
while True:
    text = input('Введите что-нибудь:')
    if text == 'выход' or text == 'exit':
        break
    if len(text) < 3:
        print ('Слишком коротко')
        continue
    print('Введенная строка достаточной длины')
    
