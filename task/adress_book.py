#!/usr/bin/env python3
import pickle

class Book:
    def __init__(self):
        self.contacts = {}
        f = open('bd.bin', 'rb')
        while True:
            try:
                var = pickle.load(f)
                self.contacts[var.name] = var
            except EOFError:
                break
        f.close()
    
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

#создать объект книги (пустую книгу)
book1 = Book()

#создать объект контакта 
contact1 = Contact.add_from_input()
contact2 = Contact.add_from_input()

#записать контакты в книгу
book1.add_contact(contact1)
book1.add_contact(contact2)
#посмотреть контакты в книге
book1.watch_contacts()
#изменить контакт 
book1.change_contact('fdk', 789)
book1.watch_contacts()
#найти контакт
book1.find_contact('fdk')
#удалить контакт
book1.del_contact('kfjgldkjl')
book1.watch_contacts()
#cохранить данные
book1.save()

print('Операции завершены')

