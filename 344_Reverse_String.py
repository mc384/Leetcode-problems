class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Left and right pointer
        l, r = 0, len(s) - 1

        while l < r:
            temp = s[l] # store s[l] in temp variable
            s[l] = s[r]
            s[r] = temp 
            l += 1
            r -= 1
