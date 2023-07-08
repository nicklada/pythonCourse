#!/usr/bin/env python3

#Создаем класс Cat с методом __init__
#Переменные _name, _color, _age - защищенные атрибуты (к ним нельзя обратиться напрямую)
#Методы get_name, get_color предоставляют доступ к защищенным атрибутам

class Cat:
    def __init__(self, name, color):
        self._name = name
        self._color = color
        self._age = 0


    def meow(self):
        print('Meow')


    def get_name(self):
        return self._name


    def get_color(self):
        return self._color


    def age(self, years):
        self._age += years


Pusha = Cat('Pusha', 'red')
name = Pusha.get_name
fur = Pusha.get_color()
age = Pusha.age(5)

print('This cat is {0}, its fur is {1}, it is {2} years old'.format(name, fur, age))
Pusha.meow()