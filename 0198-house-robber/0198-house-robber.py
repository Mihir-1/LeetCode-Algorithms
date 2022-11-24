class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = cur = 0
        for n in nums:
            temp = cur
            cur = max(prev + n, cur)
            prev = temp
        return cur