#!/usr/bin/env python3
while True:
    text = input('Введите что-нибудь:')
    if text == 'выход':
        break
    print('Для отмены введите "выход"')
    print('Длина строки:', len(text))
print('Работа завершена')
