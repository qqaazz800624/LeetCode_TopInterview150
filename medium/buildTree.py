#%%

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(val=root_val)

        root_idx = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])

        return root




#%%

inorder = [9,3,15,20,7]
preorder = [3,9,20,15,7]
root_val = preorder[0]  # 3
inorder.index(root_val) # 1




#%%






#%%