from typing import List
from collections import defaultdict


def carPooling(trips: List[List[int]], capacity: int) -> bool:
    trips = sorted(trips, key=lambda l: int(str(l[1]) + str(l[2])))
    d = defaultdict(int)
    for trip in trips:
        num_passengers = trip[0]
        start = trip[1]
        end = trip[2]
        for i in range(start, end):
            d[i] += num_passengers
    vals = [val > capacity for val in list(d.values())]
    return not any(vals)


innput = [[9, 3, 6], [8, 1, 7], [6, 6, 8], [8, 4, 9], [4, 2, 9]]
sorted_input = sorted(innput, key=lambda l: int(str(l[1]) + str(l[2])))
print(sorted_input)
print(carPooling(sorted_input, 28))
