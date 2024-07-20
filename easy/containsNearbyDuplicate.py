#%%

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in hashmap and i - hashmap[num] <= k:
                return True
            hashmap[num] = i

        return False


#%%

