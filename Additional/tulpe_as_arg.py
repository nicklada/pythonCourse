#!/usr/bin/env python3
#принимает 3 аргумента - int, кортеж и словарь 
#(в кортеже и словаре м.б. несколько значений)
def creditcalc(percent, *money, **clent_phone):
    total = 0
    for i in money:
        total +=i
    credit = total + total /100 * percent
    return credit, clent_phone

print(creditcalc(10, 100, 200, 500, Nancy=123, Ashley = 456, Ben = 789))

#принимает 3 аргумента - не кортеж!
def salarycalc(basis, bonus, indexation):
    total = basis + bonus
    salary = total + total /100 * indexation
    return salary

#создаем кортеж с данными
money = (100000, 20000, 10)
#функция поймет, что мы передаем 3 элемента, а не 1, 
# т.к. оператор * распакует кортеж на 3 элемента
print(salarycalc(*money))