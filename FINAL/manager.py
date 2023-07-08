#!/usr/bin/env python3
import pickle
import book
import contact

#создать объект книги (пустую книгу)
book1 = book.Book()

#создать объект контакта 
contact1 = contact.Contact.add_from_input()
contact2 = contact.Contact.add_from_input()

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
