class Solution:
    def rob(self, nums: List[int]) -> int:
        neigh3 = neigh2 = prev = cur = 0
        # 3 2 p c
        for n in nums:
            temp = cur
            cur, temp1 = max(neigh2 + n, prev + n), prev
            prev, temp2 = temp, neigh2
            neigh2, neigh3 = temp1, temp2
        return max(prev, cur)