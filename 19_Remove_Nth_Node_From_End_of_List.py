# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        length = 1
        temp = head
        while temp.next:
            length += 1
            temp = temp.next 
        
        offset = length - n
        prev, cur = dummy, head

        for i in range(offset):
            prev = prev.next
            cur = cur.next
        
        prev.next = cur.next
        cur.next = None

        return dummy.next
