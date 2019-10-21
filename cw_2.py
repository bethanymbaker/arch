import numpy as np
import pandas as pd


# list_1 = [-100000, 0.2, 0, 2, 4]
list_1 = []
list_2 = [-np.exp(1), 1, 3, 5, 5, 5, 6, np.inf]

# print(sorted(list_1 + list_2))

new_list = []

current_index_1 = 0
current_index_2 = 0

len_1 = len(list_1)
len_2 = len(list_2)


while (current_index_1 != len_1) & (current_index_2 != len_2):
    current_val_1 = list_1[current_index_1]
    current_val_2 = list_2[current_index_2]
    if current_val_1 < current_val_2:
        new_list.append(current_val_1)
        current_index_1 += 1
    elif current_val_2 < current_val_1:
        new_list.append(current_val_2)
        current_index_2 += 1
    else:
        new_list.append(current_val_1)
        new_list.append(current_val_2)
        current_index_1 += 1
        current_index_2 += 1

if current_index_1 != len_1:
    new_list += list_1[current_index_1:]
elif current_index_2 != len_2:
    new_list += list_2[current_index_2:]


print(new_list)





