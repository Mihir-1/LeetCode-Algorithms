class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l: int, r: int, arr: List[int]) -> List[int]:
            # Exit Recursion when no partitions to be made
            if l == r:
                return arr
            
            # Partition
            m = (l + r) // 2
            mergeSort(l, m, arr)
            mergeSort(m + 1, r, arr)

            # Merge
            left = arr[l : m + 1]
            right = arr[m + 1 : r + 1]
            i, j = 0, 0
            while i < len(left) or j < len(right):
                if i == len(left): 
                    arr[l + i + j] = right[j]
                    j += 1
                else: 
                    if j == len(right) or left[i] <= right[j]:
                        arr[l + i + j] = left[i]
                        i += 1
                    else:
                        arr[l + i + j] = right[j]
                        j += 1
            return arr
        
        # Initiate
        return mergeSort(0, len(nums) - 1, nums)