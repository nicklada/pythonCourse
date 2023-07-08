#!/usr/bin/env python3
from abc import *

class Animal(metaclass=ABCMeta):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractclassmethod
    def speak(self):
        print('Hello, world!')

class Cat(Animal):
    def __init__(self, name, color, poroda):
        super().__init__(name, color)
        self.poroda = poroda
    def speak(self):
        Animal.speak()
        return 'Meow-Meow'

class Dog(Animal):
    def speak(self):
        Animal.speak()
        return 'Bow-wow'


def animal_sounds(animals):
    for animal in animals:
        print(animal.speak())

fish = Animal('Ben', 'green')
print(fish.name)
fish.speak()

pusha = Cat('Pusha', 'red')
bublik = Dog('Bublik', 'brown')
animals = [pusha, bublik]

animal_sounds(animals)
