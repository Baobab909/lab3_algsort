import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.algorithms.fibonacci import fibo, fibo_recursive
class TestFibonacci(unittest.TestCase):
    def test_fibo(self):
        # Первые числа Фибоначчи: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
        test_cases = [(0, 0), (1, 1), (2, 1), (3, 2),(4, 3),(5, 5),(6, 8),(7, 13),(8, 21),(9, 34),(10, 55)]
        for n, e in test_cases:
            with self.subTest(f"fibo_iterative({n})"):
                self.assertEqual(fibo(n), e)

    def test_fibo_recursive(self):
        test_cases = [
            (0, 0),  # F(0) = 0
            (1, 1),  # F(1) = 1
            (2, 1),  # F(2) = 1
            (3, 2),  # F(3) = 2
            (4, 3),  # F(4) = 3
            (5, 5),  # F(5) = 5
            (6, 8),  # F(6) = 8
            (7, 13),  # F(7) = 13
            (8, 21),  # F(8) = 21
            (9, 34),  # F(9) = 34
            (10, 55),  # F(10) = 55
        ]

        for n, e in test_cases:
            with self.subTest(f"fibo_recursive({n})"):
                self.assertEqual(fibo_recursive(n), e)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fibo(-1)

        with self.assertRaises(ValueError):
            fibo(-5)

        with self.assertRaises(ValueError):
            fibo_recursive(-1)

        with self.assertRaises(ValueError):
            fibo_recursive(-10)

    def test_large(self):
        test_cases = [(15, 610), (20, 6765)]
        for n, e in test_cases:
            with self.subTest(f"fibo({n})"):
                self.assertEqual(fibo(n), e)

    def test_danger(self):
        self.assertEqual(fibo(0), 0)
        self.assertEqual(fibo_recursive(0), 0)
        self.assertEqual(fibo(1), 1)
        self.assertEqual(fibo_recursive(1), 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFibonacci)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

