class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for i in range(len(res)):
                res.append(res[i] + [num])
        return res