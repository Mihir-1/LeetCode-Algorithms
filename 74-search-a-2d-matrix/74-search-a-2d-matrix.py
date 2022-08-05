class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        lr, lc = 0, 0
        rr, rc = rows - 1, cols - 1
        
        while lr != rr or lc != rc:
            if target < matrix[lr][lc] or target > matrix[rr][rc]:
                break
            mPos = ((lr * cols + lc) + (rr * cols + rc)) // 2
            mr, mc = mPos // cols, mPos % cols
            
            if target > matrix[mr][mc]:
                if mc == cols - 1:
                    lr, lc = mr + 1, 0
                else:
                    lr, lc = mr, mc + 1
            elif target < matrix[mr][mc]:
                rr, rc = mr, mc
            else:
                return True
            
        return False if matrix[lr][lc] != target else True