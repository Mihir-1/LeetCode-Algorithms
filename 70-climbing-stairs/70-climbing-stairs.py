class Solution(object):
    def climbStairs(self, n):
        cur = 1
        prev = 0
        for i in range(n):
            t = cur
            cur += prev
            prev = t
        return cur
            