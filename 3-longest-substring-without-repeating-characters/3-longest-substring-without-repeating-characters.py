class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        maxLength = 1
        l = 0
        r = 1
        for i in range (1, len(s)):
            print(s[l:r])
            while s[i] in s[l:r]:
                l += 1
            r += 1
            maxLength = max(maxLength, len(s[l:r]))
        return maxLength
                
        