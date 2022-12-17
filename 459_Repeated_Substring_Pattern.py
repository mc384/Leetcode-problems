class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        idx = 1
        while idx <= len(s)//2:
            cur = s[:idx]
            copies = len(s)//len(cur)
            if cur * copies == s:
                return True
            else:
                idx += 1
        return False 
