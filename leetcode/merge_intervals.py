def merge(intervals):
    sorted_intervals = sorted(intervals, key=lambda i: 10 * i[0] + i[1])
    merged_intervals = []
    left_interval = sorted_intervals.pop(0)
    for right_interval in sorted_intervals:
        if right_interval[0] <= left_interval[1]:
            merged_interval = [left_interval[0], right_interval[1]]
            left_interval = merged_interval
        else:
            merged_intervals.append(left_interval)
            left_interval = right_interval
    merged_intervals.append(left_interval)
    return merged_intervals


ints = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(ints))
