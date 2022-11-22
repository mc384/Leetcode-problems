class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False 

        sums = set()
        sums.add(0)

        target = sum(nums)//2

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                return True 
            for j in sums.copy():
                if nums[i] + j == target:
                    return True 
                sums.add(nums[i] + j)

            sums.add(nums[i])

        return False 
