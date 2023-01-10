class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or k == 0:
            return nums 

        res = [0] * len(nums)

        for i in range(len(nums)):
            new = i + k
            if new < len(nums):
                res[new] = nums[i]
            else:
                new = new % len(nums)
                res[new] = nums[i]
        
        for j in range(len(nums)):
            nums[j] = res[j]
        
        return nums 
