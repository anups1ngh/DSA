class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans =0
        prev = prices[0]
        for i in range(1,len(prices)):
            current = prices[i]
            if current > prev:
                ans += (current-prev)
            prev = current
        return ans