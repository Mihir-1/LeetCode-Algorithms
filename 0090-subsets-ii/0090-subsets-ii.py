class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = {}
        nums.sort()
        
        def dfs(i, cur):
            if i == len(nums):
                curr = ""
                for i in cur:
                    curr += str(i)
                res[curr] = cur
                return
            dfs(i + 1, cur + [nums[i]])
            dfs(i + 1, cur)
        
        dfs(0, [])
        return res.values()