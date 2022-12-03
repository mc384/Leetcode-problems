## Brute force
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i in range(len(nums)-1, -1, -1):
            if k == 1:
                return nums[i]
            else:
                k -= 1
## QuickSort: to be added
