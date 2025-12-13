import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'sorts'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'data_structures'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from src.algorithms.factorial import factorial, factorial_recursive
from src.algorithms.fibonacci import fibo, fibo_recursive
from src.sort.bubble_sort import bubble_sort
from src.sort.quick_sort import quick_sort
from src.sort.counting_sort import cing_sort
from src.sort.radix_sort import radix_sort
from src.sort.bucket_sort import bucket_sort
from src.sort.heap_sort import heap_sort
from src.struct.queue import Queue
from src.utils.array_gen import rand_int_aay, nearly_sorted, reverse_sorted


def main():
    """Основная функция для демонстрации работы всех алгоритмов."""

    print("=" * 50)
    print("Лабораторная работа №3: Алгоритмы и структуры данных")
    print("=" * 50)

    # Демонстрация факториала
    print("\n1. Факториал:")
    for n in [0, 1, 5, 10]:
        print(f"  factorial_iterative({n}) = {factorial(n)}")
        print(f"  factorial_recursive({n}) = {factorial_recursive(n)}")

    # Демонстрация чисел Фибоначчи
    print("\n2. Числа Фибоначчи:")
    for n in [0, 1, 5, 10]:
        print(f"  fibonacci_iterative({n}) = {fibo(n)}")
        print(f"  fibonacci_recursive({n}) = {fibo_recursive(n)}")

    # Демонстрация сортировок
    print("\n3. Сортировки:")

    test_aay = [64, 34, 25, 12, 22, 11, 90]
    print(f"  Исходный массив: {test_aay}")

    sorts = [
        ("Пузырьковая", bubble_sort),
        ("Быстрая", quick_sort),
        ("Подсчетом", cing_sort),
        ("Поразрядная", radix_sort),
        ("Пирамидальная", heap_sort),
    ]

    for name, sort_func in sorts:
        sort_a = sort_func(test_aay)
        print(f"  {name}: {sort_a}")

    # Демонстрация очереди
    print("\n4. Очередь:")
    queue = Queue()

    print("  Добавляем элементы: 1, 2, 3")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(f"  Состояние очереди: {queue}")
    print(f"  Размер очереди: {len(queue)}")

    print(f"  Первый элемент: {queue.front()}")
    print(f"  Удаляем: {queue.dequeue()}")
    print(f"  Состояние очереди после удаления: {queue}")
    print(f"  Пуста ли очередь? {queue.is_empty()}")

    # Демонстрация генераторов
    print("\n5. Генераторы тестовых данных:")

    print("  Случайный массив:", rand_int_aay(5, 1, 10, seed=42))
    print("  Почти отсортированный:", nearly_sorted(10, 3, seed=42))
    print("  Обратно отсортированный:", reverse_sorted(10))



if __name__ == "__main__":
    main()