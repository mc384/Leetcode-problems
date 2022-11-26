class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        curr = 0 
        chars = {}

        odd = False 

        for word in words:
            if word in chars:
                chars[word] += 1 
            else: 
                chars[word] = 1
        
        for i in chars:
            if i[0] == i[1]:
                if not odd: 
                    if chars[i] % 2 == 0:
                        curr += chars[i]
                    else: 
                        curr += chars[i]
                        odd = True 
                else: 
                    if chars[i] % 2 == 0:
                        curr += chars[i]
                    else:
                        curr += chars[i] - 1
                        odd = True  
            else: 
                if i[::-1] in chars: 
                    curr += min(chars[i], chars[i[::-1]])
                else: 
                    continue
        return curr * 2
        # Time: O(n)
        # Space: O(n)
