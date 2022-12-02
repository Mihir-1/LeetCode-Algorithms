class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, n = None, 0
        for num in nums:
            if n == 0:
                maj = num
            if maj == num:
                n += 1
            else:
                n -= 1
            print(maj, n)
        return maj