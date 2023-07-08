#!/usr/bin/env python3

list2 = ['яблоки', 'манго', 'морковь', 'бананы']
print('Я должен купить ', len(list2), ' покупки')

print('Покупки: ', list2)
list2.insert(4, 'рис')
print('\nТакже нужно купить ', list2[4])
print('Теперь мой список покупок', list2)

print('\nОтсортирую-ка я свой список')
list2.sort()
print('Отсортированный список покупок выглядит так: ', list2)

firstelement = list2[0]
print('\nПервое, что мне нужно купить, это ', firstelement)

del list2[0]
print('Я купил ', firstelement)
print('Теперь мой список покупок', list2)


