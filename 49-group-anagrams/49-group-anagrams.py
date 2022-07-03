class Solution(object):
    def groupAnagrams(self, strs):
        wordMap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            wordMap[tuple(count)].append(s)
        return wordMap.values()