class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = prev = cur = 0
        # 2 p c
        for n in nums:
            temp1 = cur
            cur, temp2 = max(prev2 + n, prev + n), prev
            prev, prev2 = temp1, temp2
        return max(prev, cur)