class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True 
        if len(s) > len(t):
            return False
        sIndex, tIndex = 0,0
        while sIndex < len(s) and tIndex < len(t):
            if s[sIndex] == t[tIndex]:
                if sIndex == (len(s) - 1):
                    return True 
                else:
                    sIndex += 1
                    tIndex += 1
            else:
                tIndex += 1
        return False 
