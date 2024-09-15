#%%

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = [root]

        while queue:
            size = len(queue)       # determine the size of the current level
            for i in range(size):
                node = queue.pop(0) 
                if i == size - 1:   # if it is the last node (right node) of the current level
                    result.append(node.val)   # append the right node's value to the result
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result


#%%

a = [0,1,2,3,4,5,6,7,8,9]
print(a.pop(0))
print(a.pop(0))
print(a.pop(0))

#%%






#%%