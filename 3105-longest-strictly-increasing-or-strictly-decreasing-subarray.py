class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = curInc = curDec = 1
        prev = nums[0]

        for i, num in enumerate(nums[1:]):
            if num > prev:
                curInc += 1
                res = max(res, curInc)
                curDec = 1
            elif num < prev:
                curDec += 1
                res = max(res, curDec)
                curInc = 1
            else:
                curInc = 1
                curDec = 1
            prev = num
        
        return res

'''
Time: O(n)
Space: O(1)
'''
