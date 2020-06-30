import numpy as np


def find_indices(arr, target):
    first_index = np.inf
    last_index = -np.inf
    found = False

    for idx, val in enumerate(arr):
        if val == target:
            found = True
            first_index = np.min([first_index, idx])
            last_index = np.max([last_index, idx])

    if found:
        return [first_index, last_index]
    else:
        return [-1, -1]


arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
target = 9
print(find_indices(arr, target))

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(find_indices(arr, target))
