class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        row = len(matrix)
        col = len(matrix[0])

        dp = [[0] * (col + 1) for i in range(row+1)]

        if matrix[row-1][col-1] == "1":
            dp[row-1][col-1] = 1

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if matrix[i][j] == "0":
                    continue
                prev = min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
                dp[i][j] = 1 + prev
                res = max(res, dp[i][j])
        return res**2
      # Time: O(m*n)
      # Space: O(m*n)
