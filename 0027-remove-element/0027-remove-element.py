class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[n] = num
                n += 1
        return n