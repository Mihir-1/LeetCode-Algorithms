class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        row = [n // 2 for n in row]
        diff = dict()
        swaps = 0
        
        for i in range(len(row)):
            if row[i] not in diff:
                diff[row[i]] = i
            else:
                idx = diff[row[i]]
                if idx % 2 == 1:
                    swapIdx = idx - 1
                else:
                    swapIdx = idx + 1
                if swapIdx != i:
                    tempNum = row[swapIdx]
                    row[swapIdx] = row[i]
                    row[i] = tempNum
                    diff[tempNum] = i
                    swaps += 1
        return swaps
    
        """
        Runtime: O(n)
            - double pass with swaps
        Memory: O(n)
            - hashmap
        """
                