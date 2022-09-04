class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        arr = sorted(nums)
        counter = 0
        if arr[0] != 0:
            return 0
        if arr[r] != len(nums):
            return len(nums)
        while l <= r:
            if arr[l] == counter:
                counter += 1
                l += 1
            else:
                return counter
