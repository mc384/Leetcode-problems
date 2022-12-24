class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {']':'[', ')':'(', '}':'{'}

        stack = []

        for i in s:
            if stack and (i == "]" or i == ")" or i == "}"):
                if bracket[i] == stack[-1]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(i)
        
        return False if stack else True
