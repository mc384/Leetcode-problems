class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D': 500, 'M':1000}
        res = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and nums[s[i]] < nums[s[i+1]]:
                res += nums[s[i+1]] - nums[s[i]]
                i += 2
            else: 
                res += nums[s[i]]
                i += 1
        return res 
        # Time: O(n)
        # Space: O(1)
