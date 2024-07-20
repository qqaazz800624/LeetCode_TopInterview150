#%%

class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        length = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[length] = nums[index]
                length = length + 1
        return length


#test 1
nums = [3,2,2,3]
val = 3
Solution.removeElement(nums=nums, val=val)
#%%

#test 2
nums = [0,1,2,2,3,0,4,2]
val = 2
Solution.removeElement(nums=nums, val=val)



#%%