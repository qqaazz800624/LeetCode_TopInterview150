#%%
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            sum = digits[i] + carry
            carry = 0

            if sum == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = sum
                break

        if carry == 1:
            digits.insert(0, 1)

        return digits


#%%

#digits = [9,9,9]
#digits = [1,2,3]
#digits = [4,3,2,1]
digits = [9]
Solution().plusOne(digits)

#%%

digits = [9,9,9]
digits.insert(0, 1)
digits



#%%




#%%




#%%