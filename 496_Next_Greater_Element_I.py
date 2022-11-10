class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums1):
            for j in nums2:
                if j > nums1[i] and nums2.index(j) > nums2.index(nums1[i]):
                    res.append(j)
                    break
            i += 1
            if len(res) != i:
                res.append(-1)
        return res
