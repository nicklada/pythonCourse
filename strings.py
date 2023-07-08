#!/usr/bin/env python3
#строка с одинаковыми кавычками
print ('My name is Lada - одинарные кавычки')
#строка с двойными кавычками
print("My name is Lada - двойные кавычки")

#многострочная строка
print('''
Это многострочная строка. Это её первая строка.
Это её вторая строка.
"What's your name?", - спросил я.
Он ответил: "Bond, James Bond."
''')

#объединить две строковых константы в одну строку
print('объединяю две ' 'строковых константы')

#метод format - подставляет значение переменных которые ты в него передаешь
age = 28
name = 'Lada'
print("Меня зовут {0}, мне {1} лет".format(name, age))
# то же самое можно сделать через прямое прописывание переменных в стоке через + и преобразования числовой переменной к стринговой
print('Аналогично: ' + ' Меня зовут ' + name + ' ,мне ' + str(age) + ' лет')

# индексы в скобочках указывать не обязательно
print("{} развлекается с питоном".format(name))
print('Аналогично: ' + name + ' развлекается с питоном')

# можно передавать значения переменных сразу при вызове метода format
print('{name} учит {language}'.format(name = 'Lada', language = 'python'))
