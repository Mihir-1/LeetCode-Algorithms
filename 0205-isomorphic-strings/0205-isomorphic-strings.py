class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replace = dict()
        for i, c in enumerate(s):
            r = replace.get(c, None)
            if r and t[i] != r:
                return False
            if t[i] in replace.values() and r != t[i]:
                return False
            replace[c] = t[i]
        return True