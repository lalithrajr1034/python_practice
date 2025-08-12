# we have to import a C type
import ctypes

class CustomList:
    def __init__(self):
        self.n = 0  # Count of elements
        self.capacity = 1  # Initial capacity
        self.A = self._make_array(self.capacity)  # Allocate array

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise IndexError('Index out of bounds!')
        return self.A[k]

    def append(self, item):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = item
        self.n += 1

    def _resize(self, new_capacity):
        B = self._make_array(new_capacity)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __str__(self):
        return "[" + ", ".join(repr(self.A[i]) for i in range(self.n)) + "]"
cl = CustomList()
cl.append(10)
cl.append(20)
cl.append("hello")
print(cl)       
print(len(cl))   
print(cl[1])