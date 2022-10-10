# Store indice in hash map
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ind = {}
        for i in range(len(nums)):
            if nums[i] in ind and abs(i - ind[nums[i]] <= k):
                return True
            else:
                ind[nums[i]] = i    
        return False
