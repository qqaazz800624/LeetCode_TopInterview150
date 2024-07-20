#%%

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if root is None:
#             return True
        
#         left_if_balanced, left_height = self.isBalanced(root.left)
#         if not left_if_balanced:
#             return False
        
#         right_if_balanced, right_height = self.isBalanced(root.right)
#         if not right_if_balanced:
#             return False, 0
        
#         height_diff = abs(left_height - right_height)
#         current_if_balanced = height_diff <= 1
#         current_height = max(left_height, right_height) + 1

#         return current_if_balanced, current_height


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left_if_balanced = self.isBalanced(root.left)
        if not left_if_balanced:
            return False
        
        right_if_balanced = self.isBalanced(root.right)
        if not right_if_balanced:
            return False
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        height_diff = abs(left_height - right_height)
        current_if_balanced = height_diff <= 1

        return current_if_balanced


#%%

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left_if_balanced = self.isBalanced(root.left)
        if not left_if_balanced:
            return False
        
        right_if_balanced = self.isBalanced(root.right)
        if not right_if_balanced:
            return False
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        height_diff = abs(left_height - right_height)
        current_if_balanced = height_diff <= 1

        return current_if_balanced


#%%






#%%