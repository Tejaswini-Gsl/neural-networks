import numpy as np

# Create random vector of size 20 with floats in range 1-20
arr = np.random.rand(20) * 19 +1

# Reshape the array to 4 by 5
arr = arr.reshape(4, 5)
print(arr)

# Replace max in each row by 0 (axis=1) without using for loop
arr[np.arange(4), np.argmax(arr, axis=1)] = 0

print(arr)  # Print the modified array2