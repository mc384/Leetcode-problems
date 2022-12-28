class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(idx, cur, cursum):
            if cursum > target:
                return 
            elif cursum == target:
                res.append(cur.copy())
                return
            elif idx >= len(candidates):
                return 
            else:
                cur.append(candidates[idx])
                dfs(idx, cur, cursum + candidates[idx])
                cur.pop()
                dfs(idx + 1, cur, cursum)
        
        dfs(0, [], 0)
        return res  
