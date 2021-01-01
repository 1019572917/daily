class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        buy = max(prices)
        max_profit = 0
        for i in range(len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            if max_profit < prices[i] - buy:
                max_profit = prices[i] - buy
        return max_profit
