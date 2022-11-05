class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(cur, curSum, i):
            if i == len(candidates):
                return
            if curSum + candidates[i] == target:
                res.append(cur + [candidates[i]])
            elif curSum + candidates[i] < target:
                # Include
                dfs(cur + [candidates[i]], curSum + candidates[i], i + 1)
                # Exclude -> goto next unique
                temp = candidates[i]
                while i + 1 < len(candidates) and candidates[i + 1] == temp:
                    i += 1
                if i < len(candidates):
                    dfs(cur, curSum, i + 1)
            return
            
            
        dfs([], 0, 0)
        return res