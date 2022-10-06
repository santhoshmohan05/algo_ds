# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# DP Problem - Momization Technique

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key is index, state (buying, selling)
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1,not buying)
                dp[(i,buying)] = max(buy - prices[i], cooldown)
            else:
                sell = dfs(i+2, not buying) ## i + 2 to include the colldown day
                dp[(i,buying)] = max(sell + prices[i], cooldown)
            return dp[(i,buying)]
        return dfs(0,True)

# Tabulation Method      
from collections import defaultdict
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} ## three states - buying, selling, cooldown
        dp["Buy"] = {}
        dp["Sell"] = {}
        dp["Buy"][0] = -prices[0]
        dp["Sell"][0] = 0
        for i in range(1,len(prices)):
            ### For buying in this day, you can only access from sell of i-2 and cooldown of i-1
            sell = 0 if i-2 < 0 else dp["Sell"][i-2]
            dp["Buy"][i] = max(sell - prices[i],dp["Buy"][i-1])
            ### For Selling go with either previous buy or previous sell
            dp["Sell"][i] = max(dp["Buy"][i-1]+prices[i],dp["Sell"][i-1])
        return dp["Sell"][len(prices)-1]
    