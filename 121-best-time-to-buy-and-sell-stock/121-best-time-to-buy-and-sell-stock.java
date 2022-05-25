class Solution {
    public int maxProfit(int[] prices) {
        int a = 0;
        int b = 1;
        int largestB = 0;
        int smallestA = 0;
        while (prices.length > b) {
            while (prices[a] >= prices[b] && b < prices.length - 1) {
                a++;
                b++;
            }
            // a < b
            for (int i = b; i < prices.length; i++) {
                if (prices[i] > prices[b]) {
                    b = i;
                }
            }
            for (int i = a; i < b; i++) {
                if (prices[i] < prices[a]) {
                    a = i;
                }
            }
            if (prices[b] - prices[a] > prices[largestB] - prices[smallestA]) {
                largestB = b;
                smallestA = a;
            }
            a++;
            b = a + 1;
        }
        return prices[largestB] - prices[smallestA];
    }
}