class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        l, r = 0, len(needle)

        while r <= len(haystack):
            if haystack[l:r] == needle:
                return l
            else:
                l += 1
                r += 1
        return -1 
# Time: O(n*m)
# Space: O(1)
