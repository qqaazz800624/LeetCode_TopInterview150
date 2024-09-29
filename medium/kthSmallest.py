#%%

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, node):
        if not node or self.result is not None:
            return 
        self.inorder(node.left)
        self.count += 1
        if self.count == self.k:
            self.result = node.val
            return
        self.inorder(node.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.count = 0
        self.result = None
        self.inorder(root)
        return self.result

#%%


