# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        dummy1, dummy2 = headA, headB 
        while dummy1:
            lenA += 1 
            dummy1 = dummy1.next
        while dummy2:
            lenB += 1 
            dummy2 = dummy2.next

        if lenA > lenB:
            while lenA != lenB:
                headA = headA.next 
                lenA -= 1
        if lenB > lenA:
            while lenA != lenB:
                headB = headB.next
                lenB -= 1

        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None 
