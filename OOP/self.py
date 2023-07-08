#!/usr/bin/env python3

class ITshnik:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
       print('Здравствуйте, ', self.name)
       say = input('Введите что сказать: ')
       print(say)

programmer = ITshnik('Yarik', 28)
programmer.speak()