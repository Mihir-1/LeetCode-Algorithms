class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        if total == 0:
            return 0

        curOnes = 0
        
        for j in range(total):
            curOnes += nums[j]
        
        res = len(nums)
        i = 0
        j = total - 1
        while i < len(nums):
            res = min(total - curOnes, res)
            curOnes -= nums[i]
            i += 1
            if j == len(nums) - 1:
                j = 0
            else:
                j += 1
            curOnes += nums[j]
        
        return res
            
            
        '''
        Time: O(n)
        Space: O(1)
        '''
