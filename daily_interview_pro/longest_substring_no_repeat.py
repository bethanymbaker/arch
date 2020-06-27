# Given a string, find the length of the longest substring without repeating characters.

import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# O(n2) complexity

test_string = 'abrkaabcdefghijjxxx'
len_test_string = len(test_string)

max_length = 1

st = datetime.now()
if len_test_string > 1:
    for idx_1, val_1 in enumerate(test_string[:-1:]):
        chars = [val_1]
        for idx_2, val_2 in enumerate(test_string[idx_1 + 1:]):
            if val_2 in chars:
                break
            else:
                chars.append(val_2)
        max_length = np.max([max_length, len(chars)])
delta_t = (datetime.now() - st).total_seconds()
print(f'max length of substring = {max_length}')

# Linear complexity
test_string = 'geeksforgeeks'
max_length = 0
trail = []

for val in test_string:
    if val in trail:
        idx = trail.index(val)
        trail = trail[idx + 1:]
        trail.append(val)
    else:
        trail.append(val)
    max_length = np.max([max_length, len(trail)])
print(f'max length of substring = {max_length}')
