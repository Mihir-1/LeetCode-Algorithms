class Solution(object):
    def maxProfit(self, prices):
        lowest = prices[0]
        res = 0
        for p in prices:
            lowest = min(lowest, p)
            res = max(res, p - lowest)
        return res