class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, n = None, 0
        for num in nums:
            if n == 0:
                maj = num
            n += int(maj == num) * 2 - 1
        return maj