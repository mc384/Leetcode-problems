# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        

        tail = head
        length = 1

        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        # Return head if the net rotation has no effect
        if k == 0:
            return head

        offset = length - k - 1
        newtail = head 
        while offset > 0:
            newtail = newtail.next
            offset -= 1
        
        newhead = newtail.next

        tail.next = head
        newtail.next = None
        return newhead
