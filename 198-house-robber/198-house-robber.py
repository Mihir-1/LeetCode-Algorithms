class Solution(object):
    def rob(self, nums):
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        if(len(nums) >= 2):
            dp[1] = max(dp[0], nums[1])
            i = 2
            while i < len(nums):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
                i += 1
        return dp[len(nums) - 1]