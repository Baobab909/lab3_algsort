# Лабораторная работа №3: Алгоритмы и структуры данных


## Описание проекта

Лабораторная работа по реализации основных алгоритмов и структур данных на Python. Проект включает:
- Математические функции (факториал, числа Фибоначчи)
- Алгоритмы сортировки (6 различных методов)
- Структуры данных (очередь)
- Утилиты для тестирования и бенчмаркинга

---


## Запуск

```bash
python main.py
```

Программа покажет:
- Вычисление факториала и чисел Фибоначчи
- Сортировку массивов различными методами
- Работу структуры данных "очередь"
- Генерацию тестовых данных

---

## Функции и возможности

### 1. Математические функции

#### Факториал
```python
from src.algorithms.factorial import factorial, factorial_recursive

# Итеративный метод
result = factorial(5)  # 120
# Рекурсивный метод
result = factorial_recursive(5)  # 120
```

#### Числа Фибоначчи
```python
from src.algorithms.fibonacci import fibo, fibo_recursive

# Итеративный метод
result = fibo(10)  # 55
# Рекурсивный метод
result = fibo_recursive(10)  # 55
```

### 2. Алгоритмы сортировки

#### Пузырьковая сортировка (Bubble Sort)
```python
from src.sort.bubble_sort import bubble_sort

a = [64, 34, 25, 12, 22, 11, 90]
sorted_a = bubble_sort(a)  # [11, 12, 22, 25, 34, 64, 90]
```

#### Быстрая сортировка (Quick Sort)
```python
from src.sort.quick_sort import quick_sort

a = [64, 34, 25, 12, 22, 11, 90]
sorted_a = quick_sort(a)  # [11, 12, 22, 25, 34, 64, 90]
```

#### Сортировка подсчетом (Counting Sort)
```python
from src.sort.counting_sort import cing_sort

a = [64, 34, 25, 12, 22, 11, 90]
sorted_a = cing_sort(a)  # [11, 12, 22, 25, 34, 64, 90]
```

#### Поразрядная сортировка (Radix Sort)
```python
from src.sort.radix_sort import radix_sort

a = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_a = radix_sort(a)  # [2, 24, 45, 66, 75, 90, 170, 802]
```

#### Блочная сортировка (Bucket Sort)
```python
from src.sort.bucket_sort import bucket_sort

a = [0.78, 0.17, 0.39, 0.26, 0.72]
sorted_a = bucket_sort(a)  # [0.17, 0.26, 0.39, 0.72, 0.78]
```

#### Пирамидальная сортировка (Heap Sort)
```python
from src.sort.heap_sort import heap_sort

a = [64, 34, 25, 12, 22, 11, 90]
sorted_a = heap_sort(a)  # [11, 12, 22, 25, 34, 64, 90]
```

### 3. Структуры данных

#### Очередь (Queue)
```python
from src.struct.queue import Queue
# Создание очереди
queue = Queue()

# Добавление элементов
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Просмотр первого элемента
first = queue.front()  # 1

# Удаление элементов
item1 = queue.dequeue()  # 1
item2 = queue.dequeue()  # 2

# Проверка состояния
is_empty = queue.is_empty()  # False
size = queue.size()  # 1
```

### 4. Утилиты

#### Генераторы тестовых данных
```python
from src.utils.array_gen import (
    rand_int_aay,
    nearly_sorted,
    reverse_sorted,
    many_duplicates
)
# Случайный массив
arr1 = rand_int_aay(10, 1, 100)

# Почти отсортированный массив
arr2 = nearly_sorted(10, 3)

# Обратно отсортированный массив
arr3 = reverse_sorted(10)

# Массив с дубликатами
arr4 = many_duplicates(10, 3)
```

#### Бенчмаркинг
```python
from src.utils.benchmark import benchmark_sorts
from src.sort.bubble_sort import bubble_sort
from src.sort.quick_sort import quick_sort

# Создание тестовых данных
a = {
    "random": [64, 34, 25, 12, 22, 11, 90],
    "sorted": [1, 2, 3, 4, 5],
    "reverse": [5, 4, 3, 2, 1],
}
# Запуск бенчмарка
results = benchmark_sorts(a, {
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
})
```


##  Ограничения 

### Математические функции
- Факториал: только для неотрицательных целых чисел
- Числа Фибоначчи: только для неотрицательных целых чисел

### Сортировки
- Counting Sort: только для целых чисел
- Radix Sort: только для неотрицательных целых чисел
- Bucket Sort: оптимален для чисел в диапазоне [0, 1)

### Структуры данных
- Queue.dequeue(): IndexError при попытке удалить из пустой очереди
- Queue.front(): IndexError при попытке просмотреть пустую очередь



