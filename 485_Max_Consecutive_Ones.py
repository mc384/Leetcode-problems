class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        most = 0
        current = 0
        for i in nums: 
            if i == 1:
                current += 1
            else:
                current = 0 
            most = max(most, current)
        return most
