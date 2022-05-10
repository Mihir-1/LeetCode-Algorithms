class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        while (h - l > 1):
            m = (h + l) / 2
            if nums[m] > nums[h]:
                if nums[l] <= target and target < nums[m] :
                    h = m
                else:
                    l = m
            else:
                if  nums[m] <= target and target <= nums[h]:
                    l = m
                else:
                    h = m
                
        if nums[h] == target:
            return h
        elif nums[l] == target:
            return l
        else:
            return -1