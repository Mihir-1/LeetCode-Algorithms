class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0

        while s != f or s == 0:
            s = nums[s]
            f = nums[nums[f]]
        
        s2 = 0
        while s != s2:
            s = nums[s]
            s2 = nums[s2]

        return s