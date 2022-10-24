class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(remaining, cur):
            if len(remaining) == 0:
                res.append(cur)
                return
            for val in remaining:
                newRemaining = remaining.copy()
                newRemaining.remove(val)
                dfs(newRemaining, cur + [val])
        
        dfs(set(nums), [])
        return res