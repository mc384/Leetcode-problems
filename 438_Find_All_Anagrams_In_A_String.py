class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        res = []
        pCount = Counter(p)
        sCount = Counter(s[0:len(p)])

        if sCount == pCount:
            res.append(0)

        start, end = 1, len(p)
        while end < len(s):
            sCount[s[start-1]] -= 1
            sCount[s[end]] = 1 + sCount.get(s[end], 0)
            if sCount == pCount:
                res.append(start)
            start += 1 
            end += 1
        return res
