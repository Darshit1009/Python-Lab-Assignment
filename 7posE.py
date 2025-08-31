import numpy as np

arr = np.array([1, 2, 3, 4, 5])
memory_size = arr.size * arr.itemsize
print(f"Memory size of the array in bytes: {memory_size}")
