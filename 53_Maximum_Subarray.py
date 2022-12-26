class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cur, res = nums[0], nums[0]

        for i in range(1, len(nums)):
            if cur <= 0 and cur <= nums[i]:
                cur = nums[i]
            else:
                cur += nums[i]
            res = max(cur, res)
        return res 
