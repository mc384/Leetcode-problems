## Bottom up

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = list(range(1, n+1))

        i = 2
        while i < n:
            steps[i] = steps[i-1] + steps[i-2]
            i += 1
        return steps[n-1]
