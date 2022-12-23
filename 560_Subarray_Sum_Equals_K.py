class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = 0
        pref = {0 : 1}
        res = 0

        for i in nums:
            presum += i
            diff = presum - k
            if diff in pref:
                res += pref[diff]
            pref[presum] = 1 + pref.get(presum, 0)
        return res 
