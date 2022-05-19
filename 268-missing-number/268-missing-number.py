class Solution(object):
    def missingNumber(self, nums):
        numSet = set()
        for i in range (0, len(nums) + 1):
            numSet.add(i)
        for num in nums:
            numSet.remove(num)
        return numSet.pop()
        