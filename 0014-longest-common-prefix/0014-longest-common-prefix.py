class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for s in strs:
            i = 0
            while i < len(pre) and i < len(s) and pre[i] == s[i]:
                i += 1
            pre = pre[:i]
        return pre