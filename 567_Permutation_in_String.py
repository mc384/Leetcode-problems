# Sliding Window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        h1 = {}
        h2 = {}

        for i in range(len(s1)):
            char1 = s1[i]
            char2 = s2[i]
            h1[char1] = 1 + h1.get(char1, 0)
            h2[char2] = 1 + h2.get(char2, 0)
        
        l, r = 0, len(s1)-1

        while r < len(s2):
            perm = True
            for char in h1:
                if char in h2 and h1[char] == h2[char]:
                    continue
                else:
                    perm = False
                    break
            if perm: 
                return True
            else:
                if (r + 1) < len(s2):
                    old = s2[l]
                    h2[old] -= 1
                    l += 1
                    r += 1
                    new = s2[r]
                    h2[new] = 1 + h2.get(new, 0)
                else:
                    return False
