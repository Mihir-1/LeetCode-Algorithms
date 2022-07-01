class Solution(object):
    def isAnagram(self, s, t):
        letterMap = dict()
        for i in range (0, len(s)):
            if (s[i] in letterMap):
                letterMap.update({s[i]: (letterMap.get(s[i]) + 1)}) 
            else:
                letterMap.update({s[i]: 1})
        
        for i in range (0, len(t)):
            if (t[i] in letterMap):
                if (letterMap.get(t[i]) == 1):
                    letterMap.pop(t[i])
                else:
                    letterMap.update({t[i] : (letterMap.get(t[i]) - 1)})
            else:
                return False
        if len(letterMap.keys()) == 0:
            return True
        return False        