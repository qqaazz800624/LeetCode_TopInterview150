#%%

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_pointer = 0
        end_pointer = len(numbers) - 1

        while start_pointer < end_pointer:
            sum = numbers[start_pointer] + numbers[end_pointer]
            if sum == target:
                return [start_pointer+1, end_pointer+1]
            elif sum < target:
                start_pointer = start_pointer + 1
            else:
                end_pointer = end_pointer - 1

        return [-1, -1]


#%%





#%%