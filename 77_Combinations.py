# Backtracking DFS
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(num, cur):
            if len(cur) == k:
                res.append(cur.copy())
                return
            elif num > n:
                return
            else:
                cur.append(num)
                dfs(num + 1, cur)
                cur.pop()
                dfs(num + 1, cur)
        
        dfs(1, [])
        return res
