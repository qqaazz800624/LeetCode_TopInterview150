#%%

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if root.left is None and root.right is None:
            check = targetSum == root.val
            return check
        
        left_path_check = self.hasPathSum(root.left, targetSum - root.val)
        right_path_check = self.hasPathSum(root.right, targetSum - root.val)
        return left_path_check or right_path_check


#%%






#%%





#%%