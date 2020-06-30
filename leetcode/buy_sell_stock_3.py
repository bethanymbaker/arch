import numpy as np

arr = np.array([1, 2, 4, 2, 5, 7, 2, 4, 9, 0])
diffs = np.diff(arr)
profits = []
profit = 0
for diff in diffs:
    if diff >= 0:
        profit += diff
    else:
        profits.append(profit)
        profit = 0
print(profits)

profits = []
for idx, val in enumerate(arr):
    left = arr[:idx]
    right = arr[idx:]
    try:
        minn = min(left)
        maxx = max(right)
        if maxx >= minn:
            profits.append(maxx - minn)
    except:
        pass
