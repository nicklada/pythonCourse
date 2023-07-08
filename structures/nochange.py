#!/usr/bin/env python3
#int неизменяемый класс
a = 10
b = a
print(id(a))
#при изменении переменной id укажет, 
#что теперь объект а хранится в другой ячейке памяти
a += 2
print(id(a))
print(id(b))
print(a)
print(b)

#list - изменяемый
list = [1, 2, 3]
print(id(list))
#при изменении переменной id укажет, 
#что теперь объект а хранится в той же ячейке памяти
list [1] = 3
print(id(list))
newlist = list
print(id(newlist))