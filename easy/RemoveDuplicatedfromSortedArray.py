#%%

class Solution:
    def removeDuplicates(nums: list[int]) -> int:
        if not nums:
           return 0
       
        left = 0
    
        for right in range(len(nums)):
           if nums[left] != nums[right]:
            left = left + 1
            nums[left] = nums[right]
        
        return left + 1



#%%

# test1
test1 = [1,1,2]

# test 2
test2 = [0,0,1,1,1,2,2,3,3,4]



Solution.removeDuplicates(nums=test2)



#%%





#%%