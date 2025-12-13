def heap_sort(a: list[int]) -> list[int]:
    """
    Сортирует массив методом пирамидальной сортировки
    """
    a_copy = a.copy()
    n = len(a_copy)

    for i in range(n // 2 - 1, -1, -1):
        for_heap(a_copy, n, i)
    for i in range(n - 1, 0, -1):
        a_copy[0], a_copy[i] = a_copy[i], a_copy[0]
        for_heap(a_copy, i, 0)
    return a_copy


def for_heap(a: list, n: int, i: int) -> None:
    """
    Преобразует поддерево в кучу
    """
    big = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[big]:
        big = left
    if right < n and a[right] > a[big]:
        big = right
    if big != i:
        a[i], a[big] = a[big], a[i]
        for_heap(a, n, big)
