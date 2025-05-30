class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        windowSum = sum(cardPoints[:n-k])
        res = total - windowSum

        for i in range(k):
            windowSum += cardPoints[i + n - k] - cardPoints[i]
            res = max(total - windowSum, res)

        return res
        
        '''
        Time: O(n)
        Space: O(1)
        '''
