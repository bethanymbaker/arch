from functools import reduce
import numpy as np

arr = np.random.randint(-100, 100, 100)
arr_list = [[val] for val in arr]


def merge_sorted_lists(list_1, list_2):
    index_1 = 0
    index_2 = 0
    new_list = []
    while (index_1 < len(list_1)) & (index_2 < len(list_2)):
        val_1 = list_1[index_1]
        val_2 = list_2[index_2]
        if val_1 <= val_2:
            new_list.append(val_1)
            index_1 += 1
        else:
            new_list.append(val_2)
            index_2 += 1
    if index_1 < len(list_1):
        new_list += list_1[index_1:]
    if index_2 < len(list_1):
        new_list += list_2[index_2:]
    return new_list


# merge_sorted_lists([1, 3, 5], [2, 4])

res = reduce(merge_sorted_lists, arr_list)
