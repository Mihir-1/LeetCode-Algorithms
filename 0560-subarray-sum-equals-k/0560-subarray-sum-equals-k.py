class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        count = 0
        sums = {0 : 1}
        for num in nums:
            total += num
            if sums.get(total - k, 0) > 0:
                count += sums[total - k]
            sums[total] = 1 + sums.get(total, 0)
        return count