import numpy as np
# Create a 2D array with positive and negative numbers
mat = np.array([[ 5, -2, 3],
                [-1, 4, -6]])
# Use np.where() to replace negative numbers with 0
# The condition is 'mat < 0'
# If True, use 0
# If False, use the original value (mat)
result = np.where(mat < 0, 0, mat)
print("Original array:")
print(mat)
print("\nArray after replacing negative numbers with 0:")
print(result)

