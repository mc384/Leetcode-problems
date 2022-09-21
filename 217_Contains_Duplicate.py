# Looping using dictionary
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        for j in counts:
            if counts[j] >= 2:
                return True
        return False

        

        

## Test Cases
# containsDuplicate([1]) returns False
# containsDuplicate([1,1]) returns True
# containsDuplicate([9,8,7,6,5,4,3,2,1]) returns False
# containsDuplicate([5,4,3,2,3]) returns True
