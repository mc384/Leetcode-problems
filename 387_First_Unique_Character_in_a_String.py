class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}
        loc = -1
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = 1
            else:
                letters[s[i]] += 1
        for j in range(len(s)):
            if letters[s[j]] == 1:
                loc = j
                break
        return loc
