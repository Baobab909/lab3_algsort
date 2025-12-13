import random
from typing import Optional, List


def rand_int_aay(n: int, low: int, high: int,
                   distinct: bool = False,
                   seed: Optional[int] = None) -> List[int]:
    """
    Генерирует массив случайных целых чисел.

    Args:
        n (int): Количество элементов
        low (int): Нижняя граница (включительно)
        high (int): Верхняя граница (включительно)
        distinct (bool): Все элементы должны быть уникальны
        seed (int): Seed для генератора случайных чисел

    Returns:
        List[int]: Сгенерированный массив
    """
    if seed is not None:
        random.seed(seed)

    if distinct and (high - low + 1) < n:
        raise ValueError("Невозможно сгенерировать уникальные элементы в заданном диапазоне")

    if distinct:
        return random.sample(range(low, high + 1), n)
    else:
        return [random.randint(low, high) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, seed: Optional[int] = None) -> List[int]:
    """
    Генерирует почти отсортированный массив.

    Args:
        n (int): Количество элементов
        swaps (int): Количество пар элементов для обмена
        seed (int): Seed для генератора случайных чисел

    Returns:
        List[int]: Почти отсортированный массив
    """
    if seed is not None:
        random.seed(seed)

    a = list(range(n))

    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        a[i], a[j] = a[j], a[i]

    return a


def reverse_sorted(n: int) -> List[int]:
    """
    Генерирует обратно отсортированный массив.

    Args:
        n (int): Количество элементов

    Returns:
        List[int]: Обратно отсортированный массив
    """
    return list(range(n - 1, -1, -1))


def many_duplicates(n: int, k_unique: int = 5,
                    seed: Optional[int] = None) -> List[int]:
    """
    Генерирует массив с большим количеством дубликатов.

    Args:
        n (int): Количество элементов
        k_unique (int): Количество уникальных элементов
        seed (int): Seed для генератора случайных чисел

    Returns:
        List[int]: Массив с дубликатами
    """
    if seed is not None:
        random.seed(seed)

    unique_values = list(range(k_unique))
    return [random.choice(unique_values) for _ in range(n)]