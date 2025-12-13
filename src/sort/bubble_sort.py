def bubble_sort(a: list[int]) -> list[int]:
    """
    Сортирует массив методом пузырьковой сортировки
    """
    n = len(a)
    a_copy = a.copy()

    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            if a_copy[j] > a_copy[j + 1]:
                a_copy[j], a_copy[j + 1] = a_copy[j + 1], a_copy[j]
                flag = True

        # Если массив отсортирован
        if not flag:
            break

    return a_copy

