# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        res = n 
        first = 1
        last = n
        while first < last: 
            middle = (first+last)//2
            if isBadVersion(middle): 
                res = min(res, middle)
                last = middle 
            else: 
                first = middle + 1
        return res
