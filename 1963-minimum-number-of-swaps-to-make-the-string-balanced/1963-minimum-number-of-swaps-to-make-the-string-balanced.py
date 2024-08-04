class Solution:
    def minSwaps(self, s: str) -> int:
        count, deviation = 0, 0
        for c in s:
            inc = 1 if c == ']' else - 1
            count += inc
            deviation = max(count, deviation)
        return (deviation + 1) // 2