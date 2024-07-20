#%%

strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
            
def longest_common_prefix(strs):
    prefix = min(strs, key=len)
    strs.pop(strs.index(prefix))
    for str in strs:
        while str.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

longest_common_prefix(strs)




#%%






#%%






#%%