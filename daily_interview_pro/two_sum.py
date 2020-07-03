import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

sizez = [10 ** val for val in range(10)]
timez = []
for s in sizez:
    st = datetime.now()
    arr = np.random.randint(-100, 100, s)
    target = np.random.randint(-200, 200, 1)[0]

    d = {}
    res = []
    for idx, val in enumerate(arr):
        to_find = target - val
        if to_find in d:
            res = [d[to_find], idx]
            break
        else:
            d[val] = idx
    timez.append((datetime.now() - st).total_seconds())

plt.scatter(x=sizez, y=timez)
plt.grid()
