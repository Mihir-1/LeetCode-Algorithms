class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validPalindromeHelper(l: int, r: int):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if s[r - 1] == s[l] or s[l + 1] == s[r]:
                    a = validPalindromeHelper(l + 1, r)
                    b = validPalindromeHelper(l, r - 1)
                    return a or b
                else:
                    return False
            else:
                l += 1
                r -= 1
        return True
