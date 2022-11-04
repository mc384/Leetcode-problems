# Recursion
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

# Tabulation
class Solution:
    def fib(self, n: int) -> int:
        fibs = [0,1,1]
        i = 3 
        while i <= n:
            fibs.append(fibs[i-1] + fibs[i-2])
            i += 1
        return fibs[n]
