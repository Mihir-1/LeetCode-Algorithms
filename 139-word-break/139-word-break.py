class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [True] * (len(s) + 1)
        i = len(s) - 1
        while i >= 0:
            for word in wordDict:
                if word == s[i:i + len(word)] and dp[i + len(word)] == True:
                    dp[i] = True
                    break
                else:
                    dp[i] = False
            i -= 1
        return dp[0]
        