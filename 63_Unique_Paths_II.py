class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        res = [[0 for i in range(n+1)] for j in range(m+1)]

        res[m-1][n] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i+1][j] + res[i][j+1]
        return res[0][0]
