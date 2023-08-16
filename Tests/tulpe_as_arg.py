#!/usr/bin/env python3
#принимает 3 аргумента - int, кортеж и словарь 
#(в кортеже и словаре м.б. несколько значений)
import unittest

class Calculator:
    def creditcalc(self, percent, *money, **client_phone):
        total = 0
        for i in money:
            total +=i
        credit = total + total /100 * percent
        return credit, client_phone

#принимает 3 аргумента - не кортеж!
    def salarycalc(self, basis, bonus, indexation):
        total = basis + bonus
        salary = total + (total /100 * indexation)
        return salary

#проверим кредитный калькулятор
#print(Calculator.creditcalc(10, 100, 200, 500, Nancy=123))

#создаем кортеж с данными
#money = (100000, 20000, 10)
#функция поймет, что мы передаем 3 элемента, а не 1, 
# т.к. оператор * распакует кортеж на 3 элемента
#print(Calculator.salarycalc(*money))

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_sunny_day_credit(self):
        actual = self.calculator.creditcalc(20, 300, Anna=7345)
        expected = (360.0, {'Anna': 7345})
        self.assertEqual(actual, expected)

    def test_credit_many_payments(self):
        actual = self.calculator.creditcalc(20, 300, 200, 300, Anna=7345, Bella=4939)
        expected = (960.0, {'Anna': 7345, 'Bella':4939})
        self.assertEqual(actual, expected)

    def test_salary(self):
        actual = self.calculator.salarycalc(100000, 20000, 10)
        expected = 132000.0
        self.assertEqual(actual, expected)
    

if __name__ == '__main__':
    unittest.main()