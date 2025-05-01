class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        freq = dict()
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        res = []

        # perm: current permutation
        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in freq.keys():
                if freq[num] >= 1:
                    perm.append(num)
                    freq[num] -= 1
                    backtrack(perm)
                    perm.pop()
                    freq[num] += 1


        backtrack([])
        return res
        
        '''
        Time: O(n! * n)
        Space: O(n! * n)
        '''
