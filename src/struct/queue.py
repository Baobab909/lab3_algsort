class Queue:
    """
    Реализация очереди (FIFO - a1 In, a1 Out) на основе списка
    """

    def __init__(self):
        """
        Инициализирует пустую очередь
        """
        self._items = []

    def enqueue(self, item) -> None:
        """
        Добавляет элемент в конец очереди.
        Args:
            item: элемент для добавления
        """
        self._items.append(item)

    def dequeue(self):
        """
        Удаляет и возвращает первый элемент очереди
        """
        if self.is_empty():
            raise IndexError("Невозможно удалить элемент из пустой очереди")
        return self._items.pop(0)

    def front(self):
        """
        Возвращает первый элемент очереди без удаления
        """
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._items[0]

    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь
        """
        return len(self._items) == 0

    def size(self) -> int:
        """
        Возвращает количество элементов в очереди
        """
        return len(self._items)

    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди
        """
        return self.size()

    def __str__(self) -> str:
        """
        Возвращает строковое представление очереди
        """
        return f"Queue({self._items})"