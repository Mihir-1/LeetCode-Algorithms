class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True

        increasing = True if nums[0] < nums[1] else False
        neutral = True if nums[0] == nums[1] else False

        prev = nums[1]
        for num in nums[2:]:
            if neutral:
                if num > prev:
                    increasing = True
                
                neutral = False
                if num == prev:
                    neutral = True

            if increasing and num < prev: return False
            if not increasing and num > prev: return False
            prev = num
        return True