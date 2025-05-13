class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Optimized: Cantor's diagonal, flip i'th bit at index i

        return ''.join(['1' if num[i] == '0' else '0' for i, num in enumerate(nums)])
        
        '''
        Time: O(n)
        Space: O(1)
        '''


        """
        # Brute Force: backtrack
        n = len(nums[0])
        nums = set(nums)
        
        def dfs(num, i):
            if i == n:
                res = ''.join(num)
                if res not in nums:
                    return res
                return None
            
            res = dfs(num, i + 1)
            if res: return res

            num[i] = '1'
            return dfs(num, i + 1)

        return dfs(['0'] * n, 0)

        '''
        Time: O(n^2) - early exit when res found
        Space: O(n) - call stack height
        '''
        """
