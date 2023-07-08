#!/usr/bin/env python3
name = 'Lada Nikolaeva'

#поиск в слове
if name.find('va'):
    print('It is a woman')
if 'Lada' in name:
    print('Yes, it is Lada')

#разбить по словам
print(name.split())

#проверить, с чего начинается строка
if name.startswith('La'):
    print('Lada starts with La')