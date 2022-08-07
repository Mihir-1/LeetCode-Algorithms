class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ableToEat(k):
            total = 0
            for pile in piles:
                total += pile // k + (pile % k > 0)
            return total <= h
        
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            if ableToEat(m):
                r = m
            else:
                l = m + 1
        return l