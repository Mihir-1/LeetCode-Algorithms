class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(s.strip().split(' '))
        return len(s.strip().split(' ')[-1])