class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        
        for r in range(rows):
            res = max(res, int(matrix[r][0]))
        for c in range(cols):
            res = max(res, int(matrix[0][c]))
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == "1":
                    # print(r, c)
                    # print('top', int(matrix[r - 1][c]))
                    # print('left', int(matrix[r][c - 1]))
                    # print('topleft', int(matrix[r - 1][c - 1]))
                    matrix[r][c] = min(int(matrix[r - 1][c]), int(matrix[r][c - 1]), int(matrix[r - 1][c - 1])) + 1
                    res = max(matrix[r][c], res)
        return res ** 2
    
    """
    [
    ["1","1","1","1","0"],
    ["1","1","1","1","0"],
    ["1","1","1","1","1"],
    ["1","1","1","1","1"],
    ["0","0","1","1","1"]]
    """