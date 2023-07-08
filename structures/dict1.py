#!/usr/bin/env python3

ab = {
    'Swaroop' : 'swaroop@google.com',
    'Matsumoto' : 'matz@google.com',
    'Larry' : 'larry@mail.ru'
}

print('Адрес Сварупа: ', ab['Swaroop'])
print('В адресной книге {} контакта'.format(len(ab)))

for key, value in ab.items():
    print('Контакт ', key, 'с адресом', value)