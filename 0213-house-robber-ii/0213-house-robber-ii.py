class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        first = nums[:-1]
        second = nums[1:]
        
        prev2 = prev = cur = 0
        for n in first:
            temp = cur
            cur, temp2 = max(prev + n, prev2 + n), prev
            prev, prev2 = temp, temp2
        firstMax = max(cur, prev)
        
        prev2 = prev = cur = 0
        for n in second:
            temp = cur
            cur, temp2 = max(prev + n, prev2 + n), prev
            prev, prev2 = temp, temp2
        secondMax = max(cur, prev)
        
        return max(firstMax, secondMax)