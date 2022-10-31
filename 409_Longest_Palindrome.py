class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = 0
        maxlen = 0
        counts = {}
        for i in range(len(s)):
            if s[i] not in counts: 
                counts[s[i]] = 1
                odds += 1
            else:
                counts[s[i]] += 1
                if counts[s[i]] % 2 == 0:
                    maxlen += 2
                    odds -= 1
                else:
                    odds += 1
        return maxlen if odds == 0 else maxlen + odds//odds
