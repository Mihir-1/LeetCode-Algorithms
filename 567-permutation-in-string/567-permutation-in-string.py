class Solution(object):
    def checkInclusion(self, s1, s2):
        windowSize = len(s1)
        s1Freq = {}
        
        for c in s1:
            s1Freq[c] = s1Freq.get(c, 0) + 1
        
        for l in range(len(s2) - windowSize + 1):
            r = l + windowSize
            sub = s2[l:r]
            s2Freq = {}
            for c in sub:
                s2Freq[c] = s2Freq.get(c, 0) + 1
            if s1Freq == s2Freq:
                return True
        return False
        