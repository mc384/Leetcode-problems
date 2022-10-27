# Fast and slow pointer
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head 
        while fast:
            if not fast.next:
                if fast is None: 
                    return slow.next 
                else: 
                    return slow
            else: 
                slow = slow.next 
                fast = fast.next.next 
        return slow 
