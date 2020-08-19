# Given an array of integers, say [3,5,18, 9, 10] and a corresponding probability distribution, [0.1, 0.05, 0.1, 0.45, 0.3],
# write a function to sample one element randomly as per the given probability distribution.
from numpy import random


def sample_one(int_array, probs):
    prob_list = [probs.pop(0)]
    for val in probs:
        prob_list.append(prob_list[-1] + val)

    n = random.rand()
    for idx, val in enumerate(prob_list):
        if n <= val:
            return (int_array[idx])


int_array = [3, 5, 18, 9, 10]
probs = [0.1, 0.05, 0.1, 0.45, 0.3]

print(sample_one(int_array, probs))
