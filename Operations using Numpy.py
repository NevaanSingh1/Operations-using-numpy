import numpy as np


original_arr = np.linspace(0, 9, 10, dtype=int)
print("Original Array:", original_arr)

modified_arr = np.where(original_arr % 2 != 0, -1, original_arr)
print("Modified Array (Odds replaced):", modified_arr)

two_d_arr = original_arr.reshape(2, -1)
print("2D Array (Two Rows):\n", two_d_arr)

even_sum = 0
for x in original_arr:
    if x % 2 == 0:
        even_sum += x

print("Sum of all even numbers:", even_sum)