class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        size = len(grid)
        for r in range(size):
            for c in range(size):
                if r + c == size - 1 or r == c:
                    if grid[r][c] == 0: return False
                else:
                    if grid[r][c] != 0: return False
        return True