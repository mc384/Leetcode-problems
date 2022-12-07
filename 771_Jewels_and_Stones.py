class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        jewel = {}

        for i in jewels:
            jewel[i] = 1 + jewel.get(i, 0)
        
        for j in stones:
            try:
                if jewel[j]:
                    res += 1
            except KeyError:
                continue
        return res 
    # Time: O(m)
    # Space: O(n)
