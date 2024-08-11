#%%

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        current_sum = 0
        min_len = float('inf')

        while end < len(nums):
            current_sum +=  nums[end]
            end +=  1

            while current_sum >= target:
                min_len = min(min_len, end - start)
                current_sum -=  nums[start]
                start +=  1

        if min_len != float('inf'):
            return min_len
        else:
            return 0


#%%





#%%