class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == len(grid[0]) and len(grid) == 1:
            return grid[0][0]

        row, col = len(grid), len(grid[0])

        paths = [[0]* (col+1) for i in range(row+1)]

        for i in range(row):
            paths[i][-1] = float("inf")
        
        for j in range(col):
            paths[-1][j] = float("inf")
        
        paths[-1][-2] = 0

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                paths[i][j] = grid[i][j] + min(paths[i+1][j], paths[i][j+1])

        return paths[0][0]
      
# Backtracking DP
