class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        occs = {0:0, 1:0, 2:0}
        for i in nums:
            occs[i] = 1 + occs.get(i)

        {0:2, 1:2, 2:2}

        for i in range(len(nums)):
            if occs[0] > 0:
                nums[i] = 0
                occs[0] -= 1
            elif occs[1] > 0:
                nums[i] = 1
                occs[1] -= 1
            else:
                nums[i] = 2
                occs[2] -= 1
        return nums 
        # Time: O(n)
        # Space: O(1)
