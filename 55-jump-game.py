class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Optimal - Greedy
        n = len(nums)
        stepsLeft = 0
        for i in range(n - 1):
            stepsLeft = max(nums[i], stepsLeft)
            if stepsLeft == 0:
                return False
            stepsLeft -= 1

        return True
        '''
        Time: O(n)
        Space: O(1)
        '''
        
        
        """
        # Bottom up DP
        n = len(nums)
        reachable = [False] * n
        reachable[-1] = True
        
        for i in range(n - 2, -1, -1):
            for j in range(i, min(1 + i + nums[i], n)):
                if reachable[j]:
                    reachable[i] = True
                    break
        
        return reachable[0]
        '''
        Time: O(n^2)
        Space: O(n)
        '''
        """

        """
        # Brute Force
        n = len(nums)
        reachable = [False] * n
        reachable[0] = True

        for i in range(n - 1):
            if reachable[i]:
                for j in range(i, min(1 + i + nums[i], n)):
                    reachable[j] = True

        return reachable[-1]
        '''
        Time: O(n^2)
        Space: O(n)
        '''
        """
