def fibo(n: int) -> int:
    """
    Вычисляет n-ное число Фибоначчи итеративным способом
    """
    if n < 0:
        raise ValueError("Номер должен быть неотрицательным")
    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


def fibo_recursive(n: int) -> int:
    """
    Вычисляет n-ное число Фибоначчи рекурсивным способом
    """
    if n < 0:
        raise ValueError("Номер должен быть неотрицательным")
    if n <= 1:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
