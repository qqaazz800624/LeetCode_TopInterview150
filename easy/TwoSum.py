#%% the better implementation
      
def two_sum(nums, target):
    num_map = {}  
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]  
        num_map[num] = i  
    return []  

#%%

def two_sum(nums, target):
    num_map = {}  
    for i, num in enumerate(nums):
        complement = target - num
        if complement not in num_map:
            num_map[num] = i  
        else:
            return [num_map[complement], i]  
    return []  

# Example 
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]

#%%

# Example 
nums = [2, 3, 4, 6]
target = 8
print(two_sum(nums, target))  # Output: [0, 3]

#%%
num_map = {}
nums = [2, 7, 11, 15]
target = 9

for i, num in enumerate(nums):
    complement = target - num
    num_map[num] = i
    print("Pair: ",[i, num])
    print("Complement: ",complement)
    print("Hashmap: ",num_map)

    if complement in num_map:
        print("The saved complement: ",num_map[complement])
        print("The output: ", [num_map[complement], i])


#%%