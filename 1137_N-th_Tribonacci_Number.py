class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        t0 = 0 
        t1 = 1
        t2 = 1
        res = 0 

        for i in range(3, n+1):
            res = t0 + t1 + t2 
            t0 = t1 
            t1 = t2 
            t2 = res 
        return res
        # Time: O(n)
        # Space: O(1)
