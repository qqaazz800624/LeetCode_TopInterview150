#%%

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        candidate = None

        for num in nums:
            if counter == 0:
                candidate = num
                counter = 1   # or counter += 1 should work too
            elif candidate == num:
                counter += 1
            else:
                counter -= 1
        
        return candidate



#%%





#%%





#%%