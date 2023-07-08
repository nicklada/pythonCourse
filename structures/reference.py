#!/usr/bin/env python3
print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
# mylist - лишь ещё одно имя, указывающее на тот же объект!
mylist = shoplist 

# Я сделал первую покупку, поэтому удаляю её из списка
del shoplist[0]

# Обратите внимание, что и shoplist, и mylist выводят 
# один и тот же список # без пункта "яблоко", 
# т.к. они указывают на один объект.
print('shoplist:', shoplist)
print('mylist:', mylist)
print(id(shoplist))
print(id(mylist))

print('\nКопирование при помощи полной вырезки')
# создаём копию путём полной вырезки
mylist = shoplist[:]  
# удаляем первый элемент
del mylist[0]
# Обратите внимание, что теперь списки разные
print('shoplist:', shoplist) 
print('mylist:', mylist)

print(id(shoplist))
print(id(mylist))