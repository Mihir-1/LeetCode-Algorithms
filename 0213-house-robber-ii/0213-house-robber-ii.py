class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        first = nums[:-1]
        second = nums[1:]
        
        prev = cur = 0
        for i in range(len(nums) - 1):
            temp = cur
            cur = max(cur, prev + nums[i])
            prev = temp
        
        prev = cur2 = 0
        for i in range(1, len(nums)):
            temp = cur2
            cur2 = max(cur2, prev + nums[i])
            prev = temp
        
        return max(cur, cur2)
    
        """
        Runtime: O(n)
            - 2 pass - O(2n) -> O(n)
        Memory: O(1)
            - 3 ints
        """