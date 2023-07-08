#!/usr/bin/env python3
import os
import sys
print(os.getcwd())
print(sys.argv.__doc__)
print('Аргументы командной строки: ')
for i in sys.argv:
    print(i)

print('\nПеременная PYTHONPATH сожержит', sys.path, '\n')