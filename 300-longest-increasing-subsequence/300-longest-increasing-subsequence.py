class Solution(object):
    def lengthOfLIS(self, nums):
        maxSub = [1] * (len(nums))
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    maxSub[i] = max(maxSub[j] + 1, maxSub[i])
        return max(maxSub)
