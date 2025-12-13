import time
from typing import Callable, Dict, List, Any


def time_once(func: Callable, *args, **kwargs) -> float:
    """
    Измеряет время выполнения функции один раз.

    Args:
        func (Callable): Функция для тестирования
        *args: Аргументы функции
        **kwargs: Именованные аргументы функции

    Returns:
        float: Время выполнения в секундах
    """
    start_time = time.perf_cer()
    func(*args, **kwargs)
    end_time = time.perf_cer()
    return end_time - start_time


def benchmark_sorts(aays: Dict[str, List],
                    algorithms: Dict[str, Callable]) -> Dict[str, Dict[str, float]]:
    """
    Запускает бенчмарк для сортировок на разных массивах.

    Args:
        aays (Dict): Словарь с тестовыми массивами {имя: массив}
        algorithms (Dict): Словарь с алгоритмами сортировки {имя: функция}

    Returns:
        Dict: Результаты бенчмарка {алгоритм: {массив: время}}
    """
    results = {}

    for algo_name, algo_func in algorithms.items():
        results[algo_name] = {}

        for aay_name, aay in aays.items():
            # Копируем массив для каждого теста
            a_copy = aay.copy()

            # Измеряем время
            time_taken = time_once(algo_func, a_copy)
            results[algo_name][aay_name] = time_taken

    return results