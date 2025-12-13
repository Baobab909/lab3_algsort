def cing_sort(a: list) -> list:
    """
    Сортирует массив целых чисел методом подсчета
    """
    if not a:
        return []

    min_a = min(a)
    max_a = max(a)
    size = max_a - min_a + 1
    c = [0] * size
    for n in a:
        c[n - min_a] += 1

    sort_a = []
    for i in range(size):
        sort_a.extend([i + min_a] * c[i])
    return sort_a

