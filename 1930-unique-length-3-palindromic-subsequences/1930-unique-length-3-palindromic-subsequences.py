class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # Get first and last index of each character {a: (0, 4)}
        firstLast = dict()
        for i, c in enumerate(s):
            if c not in firstLast:
                first, last = i, i
            else:
                first, last = firstLast.get(c)
                last = max(i, last)
                
            firstLast[c] = first, last

        # Add palindrome combos to count
        count = 0
        for first, last in firstLast.values():
            if last > first:
                count += len(set(s[first + 1: last]))
        
        return count