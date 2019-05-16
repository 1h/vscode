import unittest
from operator import *


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_min(self):
        """Test method min(a, b)"""
        self.assertEqual(1, min(3, 2))

    def test_mul(self):
        """Test method mul(a, b)"""
        self.assertEqual(6, mul(2, 3))

    def test_truediv(self):
        """Test method truediv(a, b)"""
        self.assertEqual(2, truediv(6, 3))
        self.assertEqual(2.5, truediv(5, 2))

if __name__ == '__main__':
    unittest.main(verbosity=2)