class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr) - 2
        while l < r:
            m = (l + r) // 2
            if arr[m - 1] < arr[m] and arr[m] < arr[m + 1]:
                l = m + 1
            else :
                r = m
        return r