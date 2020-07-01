import numpy as np


def try_to_merge(x, y):
    x_1 = x[0]
    x_2 = x[1]
    y_1 = y[0]
    y_2 = y[1]
    if y_1 < x_2:
        return [np.min([x_1, y_1]), np.max(x_2, y_2)]
    else:
        return []


# post sorting:
# Input: [[1, 3], [2, 6], [7,8]]

# Input = sorted(Input, key=lambas lst: lst[0], lst[1])
sorted_input = [[1, 3], [2, 6], [7, 8]]

merged_intervals = []
left_interval = sorted_input[0]
for right_interval in sorted_input[1:]:
    merged = try_to_merge(left_interval, right_interval)
    if len(merged) > 1:
        left_interval = merged
    else:
        merged_intervals.append(left_interval)
        left_interval = right_interval
merged_intervals.append(merged)

print(merged_intervals)

left_interval = [1, 3]
right_inteval = [2, 6]
# try_to_merge = > [1, 6]

merged_intervals = [1, 6]

left_interval = [1, 6]
right_interval = [7, 8]
# try_to_merge -> []
merged_intevals = [[1, 6], [7, 8]]

sorted_input_2 = [[1, 2], [3, 4]]
left_inteval = [1, 2]
right_interval = [3, 4]
merged

sorted_input_3 = [[1, 2], [3, 6], [4, 7]]
