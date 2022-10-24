class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [set()]
        for num in nums:
            for i in range(len(res)):
                newSet = res[i].copy()
                newSet.add(num)
                res.append(newSet)
        return res