class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: 
            return [-1, -1]
        # Find Start
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid

        if target == nums[i]:
            res = [i]
        else:
            return [-1, -1]

        # Find End
        j = len(nums) - 1
        while i < j:
            mid = math.ceil((i + j) / 2)
            if nums[mid] <= target:
                i = mid
            else:
                j = mid - 1
        
        return res + [j]

        '''    
        Time: O(log n)
        Space: O(1)
        '''
