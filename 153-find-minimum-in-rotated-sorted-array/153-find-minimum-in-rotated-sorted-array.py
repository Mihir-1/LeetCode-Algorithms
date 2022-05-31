class Solution(object):
    def findMin(self, nums):
        low = 0;
        high = len(nums) - 1
        while (high - low > 1):
            mid = (low + high) / 2
            if (nums[mid] > nums[low]):
                low = mid
            else:
                high = mid
        return min(nums[0], nums[high])
        
        
        