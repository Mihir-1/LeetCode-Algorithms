class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i, cur):
            # print(i, cur)
            if i == len(nums):
                res.append(cur)
                return
            dfs(i + 1, cur + [nums[i]])
            # Increment for Not include branch
            temp = nums[i]
            # print(i, temp)
            while i < len(nums) and nums[i] == temp:
                i += 1
            # print(i)
            dfs(i, cur)
        
        dfs(0, [])
        return res