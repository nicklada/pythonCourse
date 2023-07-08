#!/usr/bin/env python3

class DataIsEmpty(Exception):
      def __init__(self, data):
            self.data = data
    
try:
      data = input('Введите что-нибудь ')
      if not data:
        raise DataIsEmpty(data)
except DataIsEmpty:
     'Вы не ввели данные!'
else:
    print(data)