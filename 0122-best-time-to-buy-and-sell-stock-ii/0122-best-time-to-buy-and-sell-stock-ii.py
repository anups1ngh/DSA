class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        if len(prices) < 2:
            return result
        lowest = prices[0]
        for i in range(1, len(prices)):
            current = prices[i]
            if current > lowest:
                result += (current - lowest)
            lowest = current
        return result