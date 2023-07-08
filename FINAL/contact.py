#!/usr/bin/env python3

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone       
        print('Контакт создан')
    
    def add_from_input():
        name = input('Введите имя:')
        phone = input('Введите телефон:')
        contact = Contact(name, phone)
        return contact