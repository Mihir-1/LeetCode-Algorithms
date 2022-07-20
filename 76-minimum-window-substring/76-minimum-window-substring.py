class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) - 1

        minSub = s + "1"
        l = 0
        r = 0
        
        while r < len(s):
            while r < len(s) and min(tMap.values()) < 0:
                if s[r] in tMap.keys():
                    tMap[s[r]] += 1
                r += 1

            while l < r and tMap.get(s[l], 1) > 0:
                if s[l] in tMap.keys():
                    tMap[s[l]] -= 1
                l += 1
            
            if l == r or min(tMap.values()) < 0:
                break
            
            if len(s[l:r]) < len(minSub):
                minSub = s[l:r]
            
            if s[l] in tMap.keys():
                tMap[s[l]] -= 1
            l += 1
        
        return minSub if len(minSub) <= len(s) else ""