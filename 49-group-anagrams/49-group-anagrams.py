class Solution(object):
    def groupAnagrams(self, strs):
        wordMap = defaultdict(list)
        for word in strs:
            sWord = "".join(sorted(word))
            wordMap[sWord].append(word)
        return wordMap.values()