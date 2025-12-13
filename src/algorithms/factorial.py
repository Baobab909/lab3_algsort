def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n итеративным способом
    """
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    """
    Вычисляет факториал числа n рекурсивным способом
    """
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

