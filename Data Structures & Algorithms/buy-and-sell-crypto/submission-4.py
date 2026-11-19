class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        mn = prices[0]

        for sell in prices:
            mx = max(mx, sell - mn)
            mn = min(mn, sell)
        

        return mx