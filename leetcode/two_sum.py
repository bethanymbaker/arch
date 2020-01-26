from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, val_1 in enumerate(nums):
            val_2 = target - val_1
            if val_2 in d:
                # print(f'index_1 = {idx}')
                # print(f'index_2 = {dict[val_2]}')
                return sorted([idx, d[val_2]])
            else:
                d[val_1] = idx


nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums=nums, target=target))
