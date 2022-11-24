class Solution:
    def rob(self, nums: List[int]) -> int:
        neigh2 = prev = cur = 0
        # 3 2 p c
        for n in nums:
            temp1 = cur
            cur, temp2 = max(neigh2 + n, prev + n), prev
            prev, neigh2 = temp1, temp2
        return max(prev, cur)