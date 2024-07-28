class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prevP = float('inf')
        bought = False
        for i, price in enumerate(prices):
            nextP = prices[i + 1] if i < len(prices) - 1 else float('-inf')
            if prevP >= price and price < nextP:
                profit -= price
                print('bought on:', i, 'at', price)
                bought = True
            if prevP < price and price >= nextP and bought == True:
                profit += price
                print('sold on:', i, 'at', price)
                bought = False
                print('profit', profit)
            prevP = price
        return profit