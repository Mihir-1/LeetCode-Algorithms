class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        def genRows(n):
            if n == 0:
                return
            cur = res[-1]
            newRow = [1]
            for i in range(len(cur) - 1):
                newRow.append(cur[i] + cur[i + 1])
            newRow.append(1)
            res.append(newRow)
            genRows(n - 1)
        
        genRows(numRows - 1)
        return res