class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(cur, total, index):
            if total >= target or index == len(candidates):
                if total == target:
                    res.append(cur.copy())
                return
            # try same candidate again
            dfs(cur + [candidates[index]], total + candidates[index], index)
            # move to next candidate
            dfs(cur, total, index + 1)
            return
        
        dfs([], 0, 0)
        return res