#%%
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def computeHeight(self, node: Optional[TreeNode]) -> int:
        height = 0
        while node is not None:
            height += 1
            node = node.left
        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_height = self.computeHeight(root.left)
        right_height = self.computeHeight(root.right)

        if left_height == right_height:
            return 2 ** left_height + self.countNodes(root.right)
        else:
            return 2 ** right_height + self.countNodes(root.left)


#%%

