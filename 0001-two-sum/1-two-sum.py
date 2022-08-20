class Solution(object):
    def twoSum(self, nums, target):
        numsMap = dict()
        for i in range(len(nums)):
            if target - nums[i] in numsMap:
                return [i, numsMap[target - nums[i]]]
            numsMap[nums[i]] = i
        