#!/usr/bin/env python3
import unittest

class TestAssertions(unittest.TestCase):
    def test_assertEqual(self):
        a = 1+1
        b = 2
        self.assertEqual(a, b)

    def test_assertNotEqual(self):
        a = 1
        b = 2
        self.assertEqual(a, b)
    
    def test_assertTrue(self):
        a = 3
        b = 2
        self.assertEqual(a > b)
    
    def test_assertFalse(self):
        a = 1
        b = 2
        self.assertEqual(a > b)

    def test_assertIn(self):
        a = 1
        b = [1, 2, 3]
        self.assertIn(a, b)

    def test_assertRaises(self):
        a = 'kfkf'
        b = 3
        self.assertIn(ValueError, a, b)

if __name__ == '__main__':
    unittest.main()