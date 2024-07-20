#%%

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        return list(map(pattern.index, pattern)) == list(map(s.index, s))


#%%
