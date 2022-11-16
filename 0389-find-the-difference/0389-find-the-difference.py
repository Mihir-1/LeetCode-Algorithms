class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sVals = dict()
        for c in s:
            sVals[c] = sVals.get(c, 0) + 1
        for c in t:
            if c not in sVals or sVals[c] == 0: return c
            sVals[c] -= 1
            