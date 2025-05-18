class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        bCount = 0
        for c in s:
            if c == 'b':
                bCount += 1
            else:
                res = min(res + 1, bCount)
        return res
        '''
        Time: O(n)
        Space: O(1)
        '''
        
        """
        n = len(s)
        postA = [None] * (n + 1)
        postA[n] = 0
        for i in range(n - 1, -1, -1):
            postA[i] = postA[i+1]
            if s[i] == 'a':
                postA[i] += 1
        
        prevB = [None] * (n + 1)
        prevB[0] = 0

        for i in range(0, n):
            prevB[i+1] = prevB[i]
            if s[i] == 'b':
                prevB[i+1] += 1
        
        res = float('inf')
        for a, b in zip(postA, prevB):
            res = min(a + b, res)
        return res
        '''
        Time: O(n)
        Space: O(n)
        '''
        """
