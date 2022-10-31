# DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0 
        prev = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - prev)
            prev = min(prev, prices[i])
            i += 1
        return profit  
