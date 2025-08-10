# This code normalizes each row of a 2D NumPy array using broadcasting.

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

row_norms = np.linalg.norm(arr, axis=1, keepdims=True)

normalized_arr = arr / row_norms

print("Original Array:\n", arr)
print("\nRow-wise Normalized Array:\n", normalized_arr)
