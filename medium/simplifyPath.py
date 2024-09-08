#%%


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for element in path:
            if element == '..':
                if stack:
                    stack.pop()
            elif element and element != '.':
                stack.append(element)
        output = '/' + '/'.join(stack)
        return output


#%%

path = "/.../a/../b/c/../d/./"
path = path.split('/')

stack = []
for element in path:
    if element == '..':
        if stack:
            stack.pop()
    elif element and element != '.':
        stack.append(element)

stack
#%%

output = '/'.join(stack)
output


#%%