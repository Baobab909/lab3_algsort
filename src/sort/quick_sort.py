def quick_sort(a: list) -> list:
    """
    Сортирует массив методом быстрой сортировки 
    """
    if len(a) <= 1:
        return a.copy()

    k = median(a)
    left = [x for x in a if x < k]
    a2 = [x for x in a if x == k]
    right = [x for x in a if x > k]
    return quick_sort(left) + a2 + quick_sort(right)


def median(a: list):
    """
    Выбирает медиану из первого, среднего и последнего элементов
    """
    a1 = a[0]
    a2 = a[len(a) // 2]
    a3 = a[-1]
    if a1 <= a2 <= a3 or a3 <= a2 <= a1:
        return a2
    elif a2 <= a1 <= a3 or a3 <= a1 <= a2:
        return a1
    else:
        return a3

