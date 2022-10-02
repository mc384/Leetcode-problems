class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False
        # Store letters in a hash table
        letters = {}
        # Loop - create key value pairs for occurences of letters
        i = 0
        while i < len(s):
            if s[i] in letters:
                letters[s[i]] += 1
                i += 1
            else:
                letters[s[i]] = 1
                i += 1
        
        # Verify that number of letters is the same
        j = 0
        while j < len(t):
            if t[j] in letters:
                if letters[t[j]] == 0:
                    return False
                else:
                    letters[t[j]] -= 1
                    j += 1
            else:
                return False
        return True
