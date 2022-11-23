class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        first, second, third = nums[0], nums[1], nums[2]
        closest = first + second + third  
        nums.sort()

        for l in range(0, len(nums)-2):
            mid, r = l + 1, len(nums) - 1
            while mid < r:
                current = nums[l] + nums[mid] + nums[r] 
                if current == target:
                    return target 
                if abs(current - target) < abs(closest - target):
                    closest = current 
                if current - target > 0: 
                    r -= 1
                else:
                    mid += 1
