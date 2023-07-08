#!/usr/bin/env python3
# создать список
shopping = ['milk', 'chease', 'bread', 'meat', 'butter']
# обратиться к элементу списка по индексу
print(shopping[0])
#изменить элемент по индексу
shopping[1] = 'sweets'
print(shopping)
#добавить элемент в конец списка
shopping.append(15)
print(shopping)
#добавить элемент по индексу
shopping.insert(0, 'salt')
print(shopping)
#удалить элемент по индексу
del shopping[6]
print(shopping)
#удалить элемент
shopping.remove('milk')
print(shopping)

#итерация по списку
for i in shopping:
    print(i)

#вырезать часть
print(shopping)
#выведет от 2 до последнего элемента
print(shopping[2:])
#выведет 2 элемент
print(shopping[2:3])

#итерация по списку
for i in range(0,len(shopping)):
    print('{} купила'.format(shopping[0]))
    shopping.pop(0)
    print(shopping)

print('Осталось купить ', len(shopping), ' покупок')