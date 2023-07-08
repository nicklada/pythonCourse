#!/usr/bin/env python3
brics  = {'Бразилия', 'Россия', 'Индия'}

#обратиться по индексу нельзя, т.к. множества неупорядоченные
#print(brics[1])
#изменить по индексу нельзя
#brics[2] = 'Индонезия'

#добавить элемент
brics.add('Китай')

#удалить элемент
brics.remove('Индия')

#проверка наличия элемента
print ('Китай' in brics)
print('США' in brics)

#операции множественной алгебры
asian = {'Китай', 'Индонезия', 'Индия'}
#объединение
print(brics.union(asian))
#пересечение
print(brics.intersection(asian))
#разность
print(brics.difference(asian))
