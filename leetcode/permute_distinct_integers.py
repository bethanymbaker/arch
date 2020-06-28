from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        master_list = []
        for val in nums:
            nums_copy = nums.copy()
            nums_copy.remove(val)
            for lyst in self.permute(nums_copy):
                master_list.append([val] + lyst)
        return master_list
