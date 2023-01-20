class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0 
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    cur = 4
                    if j - 1 >= 0 and grid[i][j-1] > 0:
                        cur -= 1
                    if j + 1 < m and grid[i][j+1] > 0:
                        cur -= 1
                    if i - 1 >= 0 and grid[i-1][j] > 0:
                        cur -= 1
                    if i + 1 < n and grid[i + 1][j] > 0:
                        cur -= 1
                    res += cur
        return res 
