#%%


class Solution:
    def strStr(haystack: str, needle: str) -> int:
        
        if haystack == needle:
            return 0

        for position in range((len(haystack) - len(needle)) + 1):
            if haystack[position:(position+len(needle))] == needle:
                return position
        return -1


#%%

haystack = 'sadbutsad'
needle = 'sad'
Solution.strStr(haystack, needle)

#%%
        
haystack = 'leetcode'
needle = 'leeto'
Solution.strStr(haystack, needle)

#%%

haystack = 'hello'
needle = 'll'
Solution.strStr(haystack, needle)


#%%

haystack = 'a'
needle = 'a'
Solution.strStr(haystack, needle)

#%%

haystack = 'abc'
needle = 'c'
Solution.strStr(haystack, needle)


#%%



        
