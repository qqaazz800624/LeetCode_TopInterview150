#%%
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.previous = None
        self.min_diff = float('inf')

    def in_order_traversal(self, node: Optional[TreeNode]):
        if not node:
            return

        # Traverse the left subtree
        self.in_order_traversal(node.left)

        # Process the current node
        if self.previous is not None:
            self.min_diff = min(self.min_diff, node.val - self.previous)
        self.previous = node.val

        # Traverse the right subtree
        self.in_order_traversal(node.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # Start the in-order traversal from the root
        self.in_order_traversal(root)
        return self.min_diff



#%%

# Creating a sample binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Initializing the Solution class and calling the method
solution = Solution()
min_diff = solution.getMinimumDifference(root)
print(min_diff)  # Output: 1





#%%