class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l != r:
            mid = int((l + r) / 2)
            if target == nums[mid]:
                return mid
            elif target <= nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l if nums[l] == target else -1