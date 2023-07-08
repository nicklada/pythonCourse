#!/usr/bin/env python3
#определим функцию, способную принимать любое число параметров
def phonebook(a = 5, *number, **phonebook):
    print('a =', a)
    

    #проход по всем элементам кортежа
    for single_item in number:
        print('single_item', single_item)

    #проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(phonebook(10,1,2,3,Jack=1123,John=2231,Inge=1560))