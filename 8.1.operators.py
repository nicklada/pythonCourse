#!/usr/bin/env python3

#оператор сложения +
print(2+5)
print('Lada' + ' Nikolaeva')

#оператор вычитание -
print(50-24)

#умножение *
print(3*2)
print('lada'*3)

#деление /
print(4/3)

#целочисленное деление // (частное до .)
print(4//3)

#деление по модулю % (остаток)
print(8%3)

#возведение в степень **
print(2**3)

#сдвиг влево (вывод - 11100 = 28)
print(7<<2)

#сдвиг вправо (вывод 10 = 2)
print(20>>3)

#побитовое И &
print(10&3)

#побитовое ИЛИ |
print(10|3)

#побитовое ИСКЛЮЧИТЕЛЬНО ИЛИ ^
print(10^3)

#побитовое НЕ ~
print(~10)

#меньше <
print(3<2)

#больше >
print(3>2)

#меньше или равно <=
print(3<=3)

#больще или равно >=
print(3<=2)

#равно ==
a = 1
b = 1
print(a == b) #true

#не равно !=
a = 1
b = 1
print(a != b) #false

#логическое НЕ not
a = 1
b = 1
x = a == b 
print(not x) #false

#логическое И and
a = 1
b = 1
x = a == b #true
y = a != b #false
z = True
print(x and y) #false
print(x and z) #true

#логическое ИЛИ or
a = 1
b = 1
x = a == b #true
y = a != b #false
z = False
print(x or y) #true
print(y or z) #false