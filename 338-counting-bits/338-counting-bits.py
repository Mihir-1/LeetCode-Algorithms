class Solution(object):
    def countBits(self, n):
        ans = [0 for i in range(n + 1)]
        for i in range (n + 1):
            if i:
                t = i
                t = t & t - 1
                ans[i] = ans[t] + 1
        return ans
        