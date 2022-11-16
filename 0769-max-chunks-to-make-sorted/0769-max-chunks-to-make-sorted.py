class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curMax = -1
        res = 0
        for i, num in enumerate(arr):
            curMax = max(num, curMax)
            if curMax == i:
                res += 1
        return res
    
        """
        Runtime: O(n)
            - one pass
        Memory: O(1)
            - constant number of variables
        """
            