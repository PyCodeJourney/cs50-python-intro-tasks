class Jar:
    def __init__(self, capacity=12):
        self._size = 0
        self.capacity = capacity

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self._size += n
        else:
            raise ValueError("deposited cookies exceed the jar's capacity")

    def withdraw(self, n):
        if self.size >= n:
            self._size -= n
        else:
            raise ValueError("withdrawn cookies exceed jar's size")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("negative capacity value")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("more cookies then jar capacity")
        self._size = size
