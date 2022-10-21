class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for i in range(n+1)] for j in range(m+1)]

        res[m-1][n] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                res[i][j] = res[i][j+1] + res[i+1][j]

        return res[0][0]
