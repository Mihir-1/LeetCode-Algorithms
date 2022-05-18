class Solution(object):
    def countBits(self, n):
        ans = []
        for i in range (0, n + 1):
            c = 0
            while i:
                print(i, c)
                i = i & i - 1
                c += 1
            ans.append(c)
        return ans
        