
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.algorithms.factorial import factorial, factorial_recursive


class TestFactorial(unittest.TestCase):

    def test_factorial_iterative_basic(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_recursive_basic(self):
        self.assertEqual(factorial_recursive(0), 1)
        self.assertEqual(factorial_recursive(1), 1)
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(10), 3628800)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial_recursive(-5)

    def test_consistency(self):
        for n in range(0, 10):
            self.assertEqual(factorial(n), factorial_recursive(n))


if __name__ == '__main__':
    unittest.main()