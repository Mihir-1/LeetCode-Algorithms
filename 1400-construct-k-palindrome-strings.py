class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        freq = dict()
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        
        odds = 0
        for count in freq.values():
            odds += count % 2
        
        return odds <= k

    '''
    Time: O(n)
    Space: O(n)
    '''
