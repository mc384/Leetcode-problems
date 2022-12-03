class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)/2
        occs = {}

        for i in nums:
            if i in occs:
                occs[i] += 1
                if occs[i] > majority:
                    return i
            else:
                occs[i] = 1 
                if occs[i] > majority:
                    return i
