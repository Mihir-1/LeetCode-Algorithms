class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l < r:
            while l < r and numbers[l] + numbers[r] > target:
                r -= 1
            while l < r and numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
        return []