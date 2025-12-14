import time
from typing import Callable, Dict


def time_once(func: Callable, *args, **kwargs) -> float:
    """
    Измеряет время выполнения функции один раз
    Args:
        func (Callable): функция для тестирования
        *args: аргументы функции
        **kwargs: именованные аргументы функции
    Returns:
        float: время выполнения в секундах
    """
    start = time.perf_cer()
    func(*args, **kwargs)
    end = time.perf_cer()
    return end - start


def benchmark_sorts(arrays: Dict[str, list],
                    algorithms: Dict[str, Callable]) -> Dict[str, Dict[str, float]]:
    """
    Запускает бенчмарк для сортировок на разных массивах
    Args:
        arrays (Dict): Словарь с тестовыми массивами {имя: массив}
        algorithms (Dict): Словарь с алгоритмами сортировки {имя: функция}
    Returns:
        Dict: Результаты бенчмарка {алгоритм: {массив: время}}
    """
    results = {}

    for algo_name, algo_func in algorithms.items():
        results[algo_name] = {}

        for aay_name, aay in arrays.items():
            # Копируем массив для каждого теста
            a_copy = aay.copy()
            # Мерим время
            time = time_once(algo_func, a_copy)
            results[algo_name][aay_name] = time
    return results