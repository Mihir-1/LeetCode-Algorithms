class Solution(object):
    def maxProduct(self, nums):
        cMin = 1
        cMax = 1
        res = nums[0]
        for n in nums:
            temp = max(cMin * n, cMax * n, n)
            cMin = min(cMin * n, cMax * n, n)
            cMax = temp
            res = max(res, cMax)
        return res