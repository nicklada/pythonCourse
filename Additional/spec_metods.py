#!/usr/bin/env python3

class Bird:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"Птичка улетела на юг")
    
    def __eq__(self, otherbird):
        return self.age == otherbird.age

    def speak(name):
        print('Меня зовут {}, я говорю'.format(name))
    
class Duck(Bird):
    def __init__(self, name, age, flippers):
        Bird.__init__(self, name, age)
        self.flippers = flippers
        
    def speak(self, name):
        Bird.speak(name)
        print('Кря-кря')

class Chicken(Bird):
    def __init__(self, name, age, scallop):
        Bird.__init__(self, name, age)
        self.scallop = scallop
        
    def speak(self, name):
        Bird.speak(name)
        print('Куд-кудах')


bobby = Duck('bobby', 5, 2)
print(bobby.name)
bobby.speak(bobby.name)

#проверим работу __del__
del bobby

tobby = Chicken('tobby', 5, 1)
tobby.speak(tobby.name)

sobby = Duck('sobby', 5, 4)

# проверим работу __eq__
print(tobby == sobby)
#в конце выведется еще два Птичка улетела на юг т.к. автоматически 
# вызывается деструктор для второго и третьего объекта