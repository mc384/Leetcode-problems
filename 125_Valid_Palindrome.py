import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        if len(s) == 1:
            return True
        s = s.lower()
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        s = s.replace(" ", "")
        if len(s) == 0:
            return True
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
