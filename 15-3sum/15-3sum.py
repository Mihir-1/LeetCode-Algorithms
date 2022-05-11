class Solution(object):
    def threeSum(self, nums):
        if (len(nums) < 3):
            return []
        vals = dict()
        res = []
        nums.sort()
        print(nums)
        f = 0
        while f < len(nums) - 2:
            l = f + 1;
            h = len(nums) - 1
            while h - l > 0:
                if nums[f] + nums[l] + nums[h] < 0:
                    l += 1
                elif nums[f] + nums[l] + nums[h] > 0:
                    h -= 1
                else:
                    res.append([nums[f], nums[l], nums[h]])
                    h -= 1
                    while (h - l > 0 and nums[h + 1] == nums[h]):
                        h -= 1
            while (f != len(nums) - 2 and nums[f + 1] == nums[f]):
                f += 1
            f += 1
        return res