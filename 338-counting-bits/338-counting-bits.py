class Solution(object):
    def countBits(self, n):
        ans = [0 for i in range(n + 1)]
        for i in range (n + 1):
            t = i
            while t:
                t = t & t - 1
                ans[i] += 1
        return ans
        