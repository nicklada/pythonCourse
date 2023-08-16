#!/usr/bin/env python3
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):

    def test_positive_number(self):
        a = 2; b = 3
        actual = add(a, b)
        expected = 5
        self.assertEqual(actual, expected)
    
    def test_negative_number(self):
        a = 2; b = -3
        actual = add(a, b)
        expected = -1
        self.assertEqual(actual, expected)

    def test_not_number(self):
        a = 2; b = 'c'
        #add(a, b)
        self.assertRaises(TypeError, add, a, b)

#Линия кода unittest.main() является вызовом функции main() из модуля unittest. 
#Когда функция main() вызывается, она запускает все тесты, определенные в модуле. 
if __name__ == '__main__':
    unittest.main()