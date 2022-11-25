class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i, c in enumerate(s):
            # odd
            res += 1
            l, r = i - 1, i + 1
            #print(c, l, r)
            while 0 <= l and r < len(s) and s[l] == s[r]:
                res += 1
                #print(l, r)
                l -= 1
                r += 1
            #print(res, 'even')
            # even
            l, r = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                #print(s[l:r+1])
                res += 1
                l -= 1
                r += 1
        return res