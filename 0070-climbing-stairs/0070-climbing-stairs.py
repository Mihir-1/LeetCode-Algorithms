class Solution:
    def climbStairs(self, n: int) -> int:
        prev = cur = 1
        for _ in range(n - 1):
            temp = cur
            cur += prev
            prev = temp
        return cur