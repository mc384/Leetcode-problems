class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        res = 0

        for i in range(1, len(prices)):
            if prices[i] < prev:
                prev = prices[i]
            elif prices[i] == prev:
                continue
            else:
                profit = prices[i] - prev
                prev = prices[i]
                res += profit
        return res 
        # Time: O(n)
        # Space: O(1)
