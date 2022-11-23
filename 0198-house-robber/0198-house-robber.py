class Solution:
    def rob(self, nums: List[int]) -> int:
        neigh3 = neigh2 = prev = cur = 0
        # 3 2 p c
        for n in nums:
            temp = cur
            cur = max(neigh2 + n, prev + n)
            temp1 = prev
            prev = temp
            temp2 = neigh2
            neigh2 = temp1
            neigh3 = temp2
        return max(prev, cur)