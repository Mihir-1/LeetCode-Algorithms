class Solution(object):
    def countBits(self, n):
        ans = [0]
        if (not n):
            return ans
        for i in range (1, n + 1):
            t = i
            t = t & t - 1
            ans.append(ans[t] + 1)
        return ans
        