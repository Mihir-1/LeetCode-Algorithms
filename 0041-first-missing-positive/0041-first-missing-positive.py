class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            value = abs(nums[i])
            if 0 < value and value < len(nums) + 1:
                if nums[value - 1] == 0:
                    nums[value - 1] = float('-inf')
                elif nums[value - 1] > 0:
                    nums[value - 1] *= -1

        for i in range(len(nums)):
            if nums[i] >= 0: return i + 1

        return len(nums) + 1