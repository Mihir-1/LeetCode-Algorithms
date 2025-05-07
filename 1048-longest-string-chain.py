class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(reverse=True, key=len)
        chainLengths = {w: 1 for w in words}

        for i, w in enumerate(words):
            for j in range(len(w)):
                testWord = w[:j] + w[j+1:]
                if testWord in chainLengths:
                    chainLengths[testWord] = max(chainLengths[testWord], 1 + chainLengths[w])

        return max(chainLengths.values())

'''
Time: O(n * L^2)
Space: O(n)
'''
