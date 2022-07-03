class Solution(object):
    def groupAnagrams(self, strs):
        wordMap = {}
        for word in strs:
            sWord = "".join(sorted(word))
            if sWord in wordMap:
                wordMap[sWord].append(word)
            else:
                wordMap[sWord] = [word]
        return wordMap.values()