class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
                end -= 1
                continue
            else:
                i += 1
