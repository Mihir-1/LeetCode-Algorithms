class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[cur] = nums[i]
                prev = nums[i]
                cur += 1
    
        return cur

        '''
        Time: O(n)
        Space: O(1)
        '''
