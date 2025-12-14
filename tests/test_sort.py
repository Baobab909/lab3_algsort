import unittest
import sys
import os
import random

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Импортируем все алгоритмы сортировки
from src.sort.bubble_sort import bubble_sort
from src.sort.quick_sort import quick_sort
from src.sort.counting_sort import cing_sort
from src.sort.radix_sort import radix_sort
from src.sort.bucket_sort import bucket_sort
from src.sort.heap_sort import heap_sort


class TestBubbleSort(unittest.TestCase):
    """Тесты для пузырьковой сортировки"""

    def test_none(self):
        """Сортировка пустого массива"""
        arr = []
        result = bubble_sort(arr)
        self.assertEqual(result, [])

    def test_one(self):
        """Сортировка массива с одним элементом"""
        arr = [5]
        result = bubble_sort(arr)
        self.assertEqual(result, [5])

    def test_sorted(self):
        """Сортировка уже отсортированного массива"""
        arr = [1, 2, 3, 4, 5]
        result = bubble_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random(self):
        """Сортировка случайного массива"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = bubble_sort(arr)
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])

    def test_otric(self):
        """Сортировка массива с отрицательными числами"""
        arr = [-5, -1, -3, -2, -4]
        result = bubble_sort(arr)
        self.assertEqual(result, [-5, -4, -3, -2, -1])

    def test_povtor(self):
        """Сортировка массива с дубликатами"""
        arr = [5, 2, 5, 1, 2, 3]
        result = bubble_sort(arr)
        self.assertEqual(result, [1, 2, 2, 3, 5, 5])


class TestQuickSort(unittest.TestCase):
    """Тесты для быстрой сортировки"""
    def test_none(self):
        arr = []
        result = quick_sort(arr)
        self.assertEqual(result, [])

    def test_one(self):
        arr = [5]
        result = quick_sort(arr)
        self.assertEqual(result, [5])

    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = quick_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = quick_sort(arr)
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])

    def test_otric(self):
        arr = [-5, -1, -3, -2, -4]
        result = quick_sort(arr)
        self.assertEqual(result, [-5, -4, -3, -2, -1])

    def test_povtor(self):
        arr = [5, 2, 5, 1, 2, 3]
        result = quick_sort(arr)
        self.assertEqual(result, [1, 2, 2, 3, 5, 5])


class TestCountingSort(unittest.TestCase):
    """Тесты для сортировки подсчетом."""

    def test_none(self):
        arr = []
        result = cing_sort(arr)
        self.assertEqual(result, [])

    def test_one(self):
        arr = [5]
        result = cing_sort(arr)
        self.assertEqual(result, [5])

    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = cing_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = cing_sort(arr)
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])

    def test_otric(self):
        arr = [-5, -1, -3, -2, -4]
        result = cing_sort(arr)
        self.assertEqual(result, [-5, -4, -3, -2, -1])

    def test_povtor(self):
        arr = [5, 2, 5, 1, 2, 3]
        result = cing_sort(arr)
        self.assertEqual(result, [1, 2, 2, 3, 5, 5])

    def test_large(self):
        arr = [1000, 1, 100, 10, 10000]
        result = cing_sort(arr)
        self.assertEqual(result, [1, 10, 100, 1000, 10000])


class TestRadixSort(unittest.TestCase):
    """Тесты для поразрядной сортировки"""

    def test_none(self):
        arr = []
        result = radix_sort(arr)
        self.assertEqual(result, [])

    def test_one(self):
        arr = [5]
        result = radix_sort(arr)
        self.assertEqual(result, [5])

    def test_random(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        result = radix_sort(arr)
        self.assertEqual(result, [2, 24, 45, 66, 75, 90, 170, 802])

    def test_povtor(self):
        arr = [121, 432, 121, 564, 23]
        result = radix_sort(arr)
        self.assertEqual(result, [23, 121, 121, 432, 564])

    def test_large(self):
        arr = [1000, 1, 100, 10, 10000]
        result = radix_sort(arr)
        self.assertEqual(result, [1, 10, 100, 1000, 10000])

    def test_base(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        result = radix_sort(arr, b=2)  # двоичная система
        self.assertEqual(sorted(arr), result)


class TestBucketSort(unittest.TestCase):
    """Тесты для блочной сортировки"""

    def test_none(self):
        arr = []
        result = bucket_sort(arr)
        self.assertEqual(result, [])

    def test_one(self):
        arr = [0.5]
        result = bucket_sort(arr)
        self.assertEqual(result, [0.5])




    def test_same(self):
        arr = [0.5, 0.5, 0.5, 0.5]
        result = bucket_sort(arr)
        self.assertEqual(result, [0.5, 0.5, 0.5, 0.5])


class TestHeapSort(unittest.TestCase):
    """Тесты для пирамидальной сортировки"""

    def test_none(self):
        arr = []
        result = heap_sort(arr)
        self.assertEqual(result, [])

    def test_one(self):
        arr = [5]
        result = heap_sort(arr)
        self.assertEqual(result, [5])

    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = heap_sort(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_random(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        result = heap_sort(arr)
        self.assertEqual(result, [11, 12, 22, 25, 34, 64, 90])

    def test_otric(self):
        arr = [-5, -1, -3, -2, -4]
        result = heap_sort(arr)
        self.assertEqual(result, [-5, -4, -3, -2, -1])

    def test_povtor(self):
        arr = [5, 2, 5, 1, 2, 3]
        result = heap_sort(arr)
        self.assertEqual(result, [1, 2, 2, 3, 5, 5])


class TestAllSortsSameResult(unittest.TestCase):
    """Тесты для проверки, что все сортировки дают одинаковый результат"""

    def test_all_small(self):
        """Все сортировки дают одинаковый результат для небольшого массива"""
        arr = [64, 34, 25, 12, 22, 11, 90]

        results = {
            'bubble_sort': bubble_sort(arr),
            'quick_sort': quick_sort(arr),
            'cing_sort': cing_sort(arr),
            'heap_sort': heap_sort(arr),
        }
        first = list(results.values())[0]
        for name, result in results.items():
            self.assertEqual(result, first,
                             f"{name} дал другой результат")

    def test_all_povtor(self):
        """Все сортировки дают одинаковый результат с дубликатами"""
        arr = [5, 2, 5, 1, 2, 3]

        results = {
            'bubble_sort': bubble_sort(arr),
            'quick_sort': quick_sort(arr),
            'cing_sort': cing_sort(arr),
            'heap_sort': heap_sort(arr),
        }
        first = list(results.values())[0]
        for name, result in results.items():
            self.assertEqual(result, first,
                             f"{name} дал другой результат")

    def test_all_none(self):
        """Все сортировки корректно обрабатывают пустой массив"""
        arr = []

        results = {
            'bubble_sort': bubble_sort(arr),
            'quick_sort': quick_sort(arr),
            'cing_sort': cing_sort(arr),
            'heap_sort': heap_sort(arr),
        }

        for name, result in results.items():
            self.assertEqual(result, [],
                             f"{name} неверно обработал пустой массив")



if __name__ == '__main__':
    # Простой запуск всех тестов
    print("Запуск тестов сортировок...")
    unittest.main()