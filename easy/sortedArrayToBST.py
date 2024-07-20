#%%

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def BuildBST(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.BuildBST(nums, left, mid-1)
        root.right = self.BuildBST(nums, mid+1, right)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return self.BuildBST(nums, 0, len(nums)-1)


#%%





#%%






#%%





#%%