class Solution(object):
    def lengthOfLIS(self, nums):
        maxSub = [1] * (len(nums))
        for i in range(len(nums) - 2, -1, -1):
            maximum = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    maximum = max(maxSub[j] + 1, maximum)
            maxSub[i] = maximum
        return max(maxSub)
