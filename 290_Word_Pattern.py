class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        mapping = {}

        for i in range(len(pattern)):
            if pattern[i] not in mapping and words[i] in mapping.values():
                return False 
            if pattern[i] not in mapping:
                mapping[pattern[i]] = words[i]
                continue
            else:
                if mapping[pattern[i]] != words[i]:
                    return False 
        return True 
