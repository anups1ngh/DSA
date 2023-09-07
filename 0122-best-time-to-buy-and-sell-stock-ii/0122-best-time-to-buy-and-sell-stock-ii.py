class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        prev = prices[0]
        for i in range(1,len(prices)):
            if prev < prices[i]:
                ans+= (prices[i]-prev)
            prev = prices[i]
        return ans