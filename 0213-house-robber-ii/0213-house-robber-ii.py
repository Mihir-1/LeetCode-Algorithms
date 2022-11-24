class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        first = nums[:-1]
        second = nums[1:]
        
        prev = cur = 0
        for n in first:
            temp = cur
            cur = max(cur, prev + n)
            prev = temp
        
        prev = cur2 = 0
        for n in second:
            temp = cur2
            cur2 = max(cur2, prev + n)
            prev = temp
        
        return max(cur, cur2)
    
        """
        Runtime: O(n)
            - 2 pass - O(2n) -> O(n)
        Memory: O(1)
            - 3 ints
        """