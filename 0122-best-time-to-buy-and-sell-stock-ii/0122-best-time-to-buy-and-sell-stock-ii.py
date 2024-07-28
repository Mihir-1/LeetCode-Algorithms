class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize Variables
        profit = 0
        prevP = float('inf')
        bought = False
        
        # Buy/Sell at optimal points
        for i, price in enumerate(prices):
            nextP = prices[i + 1] if i < len(prices) - 1 else float('-inf')
            
            # Buy at local minima
            if prevP >= price and price < nextP:
                profit -= price
                bought = True
            
            # Sell at local maxima
            if prevP < price and price >= nextP and bought == True:
                profit += price
                bought = False
            
            prevP = price
            
        return profit