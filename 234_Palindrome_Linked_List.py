# Array
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next 
        
        for i in range(len(nums)):
            if nums[i] != nums[len(nums)-1-i]:
                return False
        return True 
      # Time: O(n)
      # Space: O(n)
      
 
