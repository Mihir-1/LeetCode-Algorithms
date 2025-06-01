class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        maj, count = 0, 0

        for num in nums:
            if maj == num or count == 0:
                count += 1
                maj = num
            else:
                count -= 1
        
        pre = [False] * (n - 1)
        count = 0
        for i in range(n - 1):
            if nums[i] == maj:
                count += 1
            else:
                count -= 1
            pre[i] = count > 0
        
        post = [False] * (n - 1)
        count = 0
        for i in range(n - 1, 0, -1):
            if nums[i] == maj:
                count += 1
            else:
                count -= 1
            post[i - 1] = count > 0

        for i, vals in enumerate(zip(pre, post)):
            if vals[0] and vals[1]:
                return i
        return -1

        '''
        Time: O(n)
        Space: O(n)
        '''
