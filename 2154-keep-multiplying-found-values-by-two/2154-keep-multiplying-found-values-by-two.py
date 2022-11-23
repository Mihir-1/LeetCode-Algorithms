class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while True:
            temp = original
            for n in nums:
                if original == n:
                    original *= 2
            if original == temp:
                break
        return original