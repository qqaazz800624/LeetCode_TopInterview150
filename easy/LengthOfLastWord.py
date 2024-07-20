#%%

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.rstrip()
        for char in reversed(s):
            if char != ' ':
                length = length + 1
            elif char == ' ' and length > 0:
                break
        
        return length

#s = "Hello World"
s = "   fly me   to   the moon  "
Solution().lengthOfLastWord(s)


#%%

class Solution:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        length = 0
        s = s.rstrip()
        for char in reversed(s):
            if char != ' ':
                length = length + 1
            elif char == ' ' and length > 0:
                break
        
        return length

#s = "Hello World"
s = "luffy is still joyboy"
Solution.lengthOfLastWord(s)



#%%



#%%




#%%