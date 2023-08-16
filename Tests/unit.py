#!/usr/bin/env python3
import unittest

class FirtsTest(unittest.TestCase):
    def setUp(self):
        # Настройка перед каждым тестом
        pass

    def tearDown(self):
        # Очистка после каждого теста
        pass

    # Метод тестирования
    def test_calculator(self):
        self.assertEqual(2+1, 3)

#при запуске модуля напрямую (а не импорте) 
# будут выполнены все тестовые кейсы, определенные в модуле
if __name__ == '__main__':
    unittest.main()