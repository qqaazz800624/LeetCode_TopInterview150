#%%

class Solution:
    def searchInsert(nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return low


#%%
    
nums = [1,3,5,6]
#target = 5
#target = 2
#target = 7
#target = 0
target = 3

Solution.searchInsert(nums, target)


#%%
    



#%%




#%%
    



#%%
    



#%%