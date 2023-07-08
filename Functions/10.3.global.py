#!/usr/bin/env python3
#переменные за пределами функции
sum = 10000
percent = 10

def creditcalk():
    # объявляем что sum, percent- это глобальные переменные
    global sum, percent
    print ('Переменная sum изначальна равна', sum)
    #переопределим глобальную переменную sum
    sum = sum + (sum/100)*percent
    print('Сумма кредита равна ', sum)

creditcalk()
#глобальная переменная sum изменилась в функции - и за ее пределами
print('Переменная sum за пределами функции ИЗМЕНИЛАСЬ и равна', sum)