class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        prev = prices[0]
        for i in range(1,len(prices)):
            current_profit = prices[i] - prev
            if prev < prices[i]:
                max_profit = max(max_profit,current_profit)
            else:
                prev = prices[i]
        return max_profit