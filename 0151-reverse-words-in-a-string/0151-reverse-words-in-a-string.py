class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(reversed([st.strip() for st in s.strip().split()])))