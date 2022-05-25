class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int lowest = prices[0];
        for (int i = 1; i < prices.length; i++) {
            lowest = Math.min(lowest, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - lowest);
        }
        return maxProfit;
    }
}