class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        loc = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in loc:
                return [i, loc[diff]]
            else:
                loc[nums[i]] = i 

        # Time: O(n)
        # Space: O(n)  
 
