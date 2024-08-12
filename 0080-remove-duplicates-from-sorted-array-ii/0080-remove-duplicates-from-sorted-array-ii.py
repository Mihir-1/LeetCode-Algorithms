class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        num = float('inf')
        count = 0
        for i in range(len(nums)):
            if nums[i] != num:
                num = nums[i]
                count = 1
                nums[k] = nums[i]
                k += 1
            elif count < 2:
                count += 1
                nums[k] = nums[i]
                k += 1
                
        return k

