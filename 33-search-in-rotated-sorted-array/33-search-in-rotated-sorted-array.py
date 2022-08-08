class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[l]:
                if nums[m] <= target and target <= nums[r]:
                    l = m
                else:
                    r = m - 1
            else:
                if nums[l] <= target and target <= nums[m]:
                    r = m
                else:
                    l = m + 1

        return l if nums[l] == target else -1