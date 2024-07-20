#%%

def isValid(s: str) -> bool:
    opening_brackets = {'(', '{', '['}
    closing_brackets = {')', '}', ']'}
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != mapping[char]:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False
    
     
test1 = "()"
test2 = "()[]{}"
test3 = "(]"
print('Test case 1 is: ',isValid(test1))
print('Test case 2 is: ',isValid(test2))
print('Test case 3 is: ',isValid(test3))


#%% simpified version

def isValid(self, s: str) -> bool:
    opening_brackets = {'(', '{', '['}
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif not stack or stack[-1] != mapping[char]:
            return False
        else:
            stack.pop()
    return not stack

test1 = "()"
test2 = "()[]{}"
test3 = "(]"
print('Test case 1 is: ',isValid(test1))
print('Test case 2 is: ',isValid(test2))
print('Test case 3 is: ',isValid(test3))


#%%



