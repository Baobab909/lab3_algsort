def bucket_sort(a: list, buckets: int = None) -> list:
    """
    Сортирует массив чисел с плавающей точкой методом блочной сортировки
    """
    if not a:
        return []

    if buckets is None:
        buckets = len(a)
    min_a = min(a)
    max_a = max(a)
    if min_a == max_a:
        return a.copy()
    buckets = [[] for i in range(buckets)]

    for num in a:
        norm = (num - min_a) / (max_a - min_a)
        bucket_index = int(norm * (buckets - 1))
        buckets[bucket_index].append(num)

    # Сортируем каждый блок и объединяем
    sort_a = []
    for b in buckets:
        sort_a.extend(sorted(b))
    return sort_a