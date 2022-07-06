class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        f = 0
        while f < len(nums) - 2:
            l = f + 1
            r = len(nums) - 1
            tgt = 0 - nums[f]
            print(f, l, r)
            while (l < r):
                while l < r and nums[l] + nums[r] > tgt:
                    r -= 1
                while l < r and nums[l] + nums[r] < tgt:
                    l += 1
                if l != r and nums[l] + nums[r] == tgt:
                    res.append([nums[f], nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    l += 1
            while f < len(nums) - 2 and nums[f + 1] == nums[f]:
                f += 1
            f += 1
        return res
                    