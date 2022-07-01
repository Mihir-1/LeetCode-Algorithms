class Solution(object):
    def containsDuplicate(self, nums):
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet.add(num)
        return False
        