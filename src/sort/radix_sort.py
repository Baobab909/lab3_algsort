def radix_sort(a: list, b: int = 10) -> list:
    """
    Сортирует массив целых чисел методом поразрядной сортировки
    """
    if not a:
        return []

    a_copy = a.copy()
    max_num = max(a_copy)

    e = 1
    while max_num // e > 0:
        a_copy = for_radix(a_copy, e)
        e *= b
    return a_copy

def for_radix(a: list, e: int) -> list:
    """
    Вспомогательная функция
    """
    n = len(a)
    output = [0] * n
    c = [0] * 10

    # Подсчитываем количество вхождений каждой цифры
    for i in range(n):
        index = (a[i] // e) % 10
        c[index] += 1

    for i in range(1, 10):
        c[i] += c[i - 1]

    i = n - 1
    while i >= 0:
        index = (a[i] // e) % 10
        output[c[index] - 1] = a[i]
        c[index] -= 1
        i -= 1
    return output


