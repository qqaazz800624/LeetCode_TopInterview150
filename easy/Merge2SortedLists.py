#%%

#Definition for singly-linked list.
class ListNode:
    def __init__(self,initdata=0):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


#%%

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Initialize a dummy ListNode that acts as the starting point of the merged list
        start = ListNode()  
        # Initialize a pointer that will be used to build the merged list
        pointer = start

        # Iterate as long as neither of the lists is exhausted
        while list1 and list2:
            # If the current node in list1 has a smaller value
            if list1.val <= list2.val:
                # Link this smaller node to the merged list
                pointer.next = list1
                # Move forward in list1
                list1 = list1.next
            else:
                # If the current node in list2 is smaller or equal, link it to the merged list
                pointer.next = list2
                # Move forward in list2
                list2 = list2.next

            # Move the pointer forward in the merged list
            pointer = pointer.next

        # After exiting the loop, link the remaining elements of the non-exhausted list
        pointer.next = list1 or list2

        # Return the head of the merged list, which is the next element after the dummy node
        return start.next  






#%%

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        # Initialize a dummy node and a tail pointer
        dummy = ListNode()
        tail = dummy

        # Initialize two pointers for each list
        pointer1 = list1
        pointer2 = list2

        # Traverse through both lists
        while pointer1 is not None and pointer2 is not None:
            if pointer1.val < pointer2.val:
                tail.next = pointer1
                pointer1 = pointer1.next  # Move pointer1 forward
            else:
                tail.next = pointer2
                pointer2 = pointer2.next  # Move pointer2 forward
                
            tail = tail.next  # Move the tail pointer forward

        # If one list is exhausted, link the remaining elements of the other list
        if pointer1 is not None:
            tail.next = pointer1
        elif pointer2 is not None:
            tail.next = pointer2

        return dummy.next  # Return the merged list, skipping the dummy node



#%%




#%%