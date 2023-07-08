#!/usr/bin/env python3

dictionary = {'Jarik' : 'Uchitelskaya 18', 'Lada' : 'Uchitelskaya 18', 'mama' : 'Lunacharskogo 106', 'papa': 'Lunacharskogo 106', 'Grisha' : 'Lunacharskogo 106'}

#доступ по ключу
print(dictionary['Lada'])

#доступ по индексу 
#невозможен, т.к. словарь неупорядоченный!
#print(dictionary[0])

#изменение по индексу также невозможно
#dictionary[0] = 'Iaroslav' 

#изменение по ключу
dictionary['Lada'] = 'Dibenko'
dictionary['Jarik'] = 'Dibenko'
print(dictionary)

#добавление пары по ключу
dictionary['Smb'] = 'Grazdansky 100'
print(dictionary)

#удаление пары по ключу
del dictionary['Smb']
print(dictionary)

#итерация по словарю
for key, value in dictionary.items():
    print(key, value)

#проверка наличия в словаре
a = 'Lada'
if a in dictionary:
    print(a)
