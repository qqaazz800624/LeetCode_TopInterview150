#%%

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        carry = 0
        current = dummy
        while l1 or l2 or carry:
            if l1:
                val_v1 = l1.val
                l1 = l1.next
            else:
                val_v1 = 0

            if l2:
                val_v2 = l2.val
                l2 = l2.next
            else:
                val_v2 = 0
            
            sum_val = val_v1 + val_v2 + carry
            carry = sum_val // 10
            new_node = ListNode(sum_val % 10)
            current.next = new_node
            current = current.next
        return dummy.next





#%%