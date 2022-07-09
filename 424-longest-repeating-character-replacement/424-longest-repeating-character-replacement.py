class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        r = 0
        freq = {}
        maxLength = 0
        
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            
            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
                            
            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength