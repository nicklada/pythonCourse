#!/usr/bin/env python3
import pickle
import os

class Book:
    def __init__(self):
        self.contacts = {}
        file_path = '/Users/lada/tmp/py/FINAL/bd.bin'
        if os.path.exists(file_path):
            with open('bd.bin', 'rb') as f:
                while True:
                    try:
                        var = pickle.load(f)
                        self.contacts[var.name] = var
                    except EOFError:
                        break
    
    def save(self):
        f = open('bd.bin', 'wb')
        for value in self.contacts.values():
                pickle.dump(value, f)
        f.close()

    def get_contacts(self):
        return self.contacts

    def add_contact(self, contact):
        self.contacts[contact.name] = contact
        print('Контакт записан')
    
    def del_contact(self, name):
        try:
            del self.contacts[name]
        except KeyError:
            print('Отсутствующий контакт не может быть удален')
    
    def change_contact(self, name, phone):
        if name in self.contacts:
            contact = self.contacts[name]
            contact.phone = phone
        else:
            print('Такого контакта нет')

    def find_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(contact.name, contact.phone)
        else:
            print('Контакт не найден')

    def watch_contacts(self):
        for value in self.contacts.values():
            name = value.name
            phone = value.phone
            print(name, phone)