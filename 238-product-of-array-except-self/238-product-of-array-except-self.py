class Solution(object):
    def productExceptSelf(self, nums):
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums), 1):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        print(left, right)
        for i in range(0, len(nums), 1):
            left[i] = left[i] * right[i]
        return left
        