class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i, c in enumerate(s):
            # odd
            #res -= 1
            l = r = i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            #even
            l, r = i, i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res