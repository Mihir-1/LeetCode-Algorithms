class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[j + 1][i + 1] = dp[j][i] + 1
                else:
                    dp[j + 1][i + 1] = max(dp[j][i + 1], dp[j + 1][i])
        print(dp)
        return dp[len(text2)][len(text1)]
                    
        
        