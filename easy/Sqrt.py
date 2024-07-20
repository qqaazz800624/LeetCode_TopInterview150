#%%

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        low = 0
        high = x

        while low <= high:
            mid = (low + high)//2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                low = mid + 1
                answer = mid
            else:
                high = mid -1

        return answer 


Solution().mySqrt(8)



#%%






#%%






#%%