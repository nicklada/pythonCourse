#!/usr/bin/env python3

class ITshnik:
    population = 0 #переменная класса
    name = 'ITshnik'

    def __init__(self, name, age):
        self.name = name #переменная объекта
        self.age = age   #переменная объекта

        ITshnik.population += 1
    
    def speak(self):
       print('Здравствуйте, ', self.name)
       say = input('Введите что сказать: ')
       print(say)
    
    #Метод howMany принадлежит классу, а не объекту т.е. это staticmethod
    @staticmethod
    def howMany():
        print('У нас {0:d} айтишничков.'.format(ITshnik.population))

programmer = ITshnik('Yarik', 28)

# переменная класса доступна как через экземпляры класса, так и через сам класс
print(programmer.population) #1
print(ITshnik.population)    #1

# переменная объекта доступна только через экземпляры класса
print(programmer.age) #28
#print(ITshnik.age) #ошибка, не можем вызавть переменную объекта у класса

#Изменение значения переменной класса отразится на всех экземплярах класса
tester = ITshnik('Lada', 28)
print(programmer.population) #2
print(tester.population)     #2

#Переменные объекта уникальны для каждого объекта
tester.age = 29
print(programmer.age) #28
print(tester.age) #29

#метод класса можем вызвать только у класса, а не у объекта
ITshnik.howMany() #2
