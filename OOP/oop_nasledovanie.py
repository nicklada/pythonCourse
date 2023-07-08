#!/usr/bin/env python3

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        raise NotImplementedError("Method 'speak' must be implemented in subclass")

class Cat(Animal):
    def speak(self):
        return 'Meow-Meow'

class Dog(Animal):
    def speak(self):
        return 'Bow-wow'


def animal_sounds(animals):
    for animal in animals:
        print(animal.speak())

pusha = Cat('Pusha', 'red')
bublik = Dog('Bublik', 'brown')

print(pusha.speak())
print(bublik.speak())