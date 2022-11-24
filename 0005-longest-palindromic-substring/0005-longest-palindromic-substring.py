class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            # odd search
            l = r = i
            while 0 <= l - 1 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            if (r - l + 1) > len(res):
                res = s[l:r+1]
            # even search
            if i < len(s) - 1 and s[i] == s[i + 1]:
                l, r = i, i + 1
                while 0 <= l - 1 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
                    l -= 1
                    r += 1
                if (r - l + 1) > len(res):
                    res = s[l:r+1]
        return res