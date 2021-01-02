class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        profit = 0
        for i in range(1,length):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
