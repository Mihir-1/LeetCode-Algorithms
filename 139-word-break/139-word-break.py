class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [True] * (len(s) + 1)
        #print dp
        i = len(s) - 1
        while i >= 0:
            for word in wordDict:
                if word == s[i:i + len(word)] and dp[i + len(word)] == True:
                    #print(i, word, s[i:i + len(word)])
                    #print(i + len(word))
                    dp[i] = True
                    break
                else:
                    dp[i] = False
            i -= 1
            #print(dp)
        return dp[0]
        