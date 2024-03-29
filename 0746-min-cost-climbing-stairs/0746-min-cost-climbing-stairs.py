class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cur = 0
        for c in cost:
            temp = cur
            cur = min(prev + c, cur + c)
            prev = temp
        return min(prev, cur)
        