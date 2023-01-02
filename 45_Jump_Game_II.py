# Dynamic Programming

class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)] * len(nums)
        dp[-1] = 0

        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= (len(nums) - i - 1):
                dp[i] = 1
                continue
            else:
                for j in range(1, nums[i] + 1):
                    if j < len(nums):
                        dp[i] = min(dp[i], 1 + dp[i + j])

        return dp[0]
# Time: O(n^2)
# Space: O(n)
