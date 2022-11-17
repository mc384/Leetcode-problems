class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        
        if len(nums1) < len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    res.add(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    res.add(nums2[i])

        return res 
