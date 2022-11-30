class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(paren, opened, closed):
            if opened + closed == (n * 2):
                res.append(paren)
            elif opened == n:
                backtrack(paren + ")", opened, closed + 1)
            elif opened == closed:
                backtrack(paren + "(", opened + 1, closed)
            else:
                backtrack(paren + "(", opened + 1, closed)
                backtrack(paren + ")", opened, closed + 1)
            
                

            
        backtrack("", 0, 0)
        
        return res 
