class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i, cur):
            if i == len(nums):
                res.append(cur)
                return
            dfs(i + 1, cur + [nums[i]])
            temp = nums[i]
            while i < len(nums) and nums[i] == temp:
                i += 1
            dfs(i, cur)
        
        dfs(0, [])
        return res